#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import sys
import http.client
import urllib.parse
import json
import hashlib
import random
from time import sleep
from datetime import datetime

# limit
max_browse_news = 5
max_comment_news = 5
max_share_news = 5

# YQ param
yq_version = 'V2.1.3'

# device
dev_name = 'GT-I8552'
registrationId = 'e7bcfcfcb94e91d52d174ffb26341532'
imei = 'DMfFJEqHRJOLmsf89I0gtg\u003d\u003d'

# servers address & port
login_server = 'common.iyouqu.com.cn:8080'
data_server = 'iyouqu.com.cn:8080'

# locate_1 关东
locate_1 = {'country': '中国',
            'province': '湖北省',
            'city': '武汉市',
            'position': '在烽火科技签到啦！',
            'longitude': 114.4342,
            'latitude': 30.5055}

# locate_2 高新四路
locate_2 = {'country': '中国',
            'province': '湖北省',
            'city': '武汉市',
            'position': '在烽火通信高新四路研发中心签到啦！',
            'longitude': 114.4302,
            'latitude': 30.4542}

# comments
comments = ['good', '[强]', 'nice']

# HTTP headers
req_headers = {
    'YQ-Version': yq_version,
    'YQ-Platform': 'android',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'common.iyouqu.com.cn:8080',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.3.1', }


class YqUser:
    user_file = 'test.txt'

    def __init__(self,name,mobile, passwd):
        self.name = name
        self.mobile = mobile
        self.passwd = passwd_hash(passwd)
        self.cookie_file = self.mobile + '.dat'
        self.group_file = self.mobile + '_group.txt'
        # self.group_file = 'batch_group.txt'

    def login(self):
        '''
        User login
        '''
        print('{} login...'.format(self.name), flush=True)

        global req_headers
        req_headers['Host'] = login_server
        if 'YQ-Token' in req_headers:
            req_headers.pop('YQ-Token')

        
        # send mobile
        req_data_val = {'mobile': self.mobile, 'msgId': 'APP127'}
        resp_data = get_resp_data('/app/user/service.do', login_server, req_headers, req_data_val,self.name)

        # send password
        req_data_val = {'device': dev_name, 'mobile': self.mobile, 'msgId': 'APP129', 'password': self.passwd,
                        'version': yq_version, 'registrationId': registrationId, 'system': '4.4.2', 'systemType': '1',
                        'pushType': 1}

        resp_data = get_resp_data('/app/user/service.do', login_server, req_headers, req_data_val,self.name)
        self.name = resp_data['resultMap']['userInfo']['name']
        self.id = resp_data['resultMap']['userInfo']['id']
        self.depart = resp_data['resultMap']['userInfo']['orgid']
        self.token = resp_data['resultMap']['userInfo']['usertoken']

        req_headers['YQ-Token'] = self.token
        # send login finished
        req_data_val = {'msgId': 'GET_OFFLINEMSG', 'userId': self.id}
        finish_data = get_resp_data('/app/group/service.do', login_server, req_headers, req_data_val,self.name)


def passwd_hash(passwd):
    '''
    Return password hash value
    '''
    m = hashlib.md5()
    m.update(passwd.encode())

    return m.hexdigest()


def get_resp_data(url, server_addr, req_header, req_data_val,name):
    '''
    Connect to server, send POST data, and
    get server response data
    '''
    req_data = urllib.parse.urlencode({'text': req_data_val})
    conn = http.client.HTTPConnection(server_addr, timeout=10)
    conn.request('POST', url, req_data, req_header)
    resp = conn.getresponse()

    # Server return OK
    if (resp.status != 200):
        raise Exception("server response status={}".format(resp.status))

    resp_data = json.loads(resp.read().decode())

    resp_code = resp_data['code']
    resp_msg = resp_data['message']

    # Get message OK
    if (resp_code != '0'):
        print('login error info:%s' %resp_msg)
        with open('log_error.txt', 'a') as f:
            f.write(req_data_val['mobile']+' '+name+':'+resp_msg+'\n')
        
    return resp_data


def wait_time(seconds):
    cnt = seconds // 10
    for i in range(cnt + 1):
        if seconds >= 10:
            sleep(10)
            seconds = seconds - 10
        else:
            sleep(seconds)
        print('>', end='', flush=True)


def main():
    try:
        if os.path.isfile(YqUser.user_file) != True:
            raise Exception('Please create file "{}"'.format(YqUser.user_file))

        with open('log_error.txt', 'w') as f:
            f.write('')

        with open(YqUser.user_file, 'r') as f:
            for line in f.readlines():
                try:
                    line=line.strip()
                    m,p, name=line.split(' ')
                    m=m.strip()
                    p=p.strip()
                    name=name.strip('\r\n')
                    user = YqUser(name,m, p)
                    user.login()
                    sleep(1)
                except Exception as e:
                    print(e)
                    continue
            
    except Exception as e:
        print('Error: ', e, ' ')
    finally:
        exit(0)
        


if __name__ == '__main__':
    main()
