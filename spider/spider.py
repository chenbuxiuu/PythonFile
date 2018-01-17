import urllib
import urllib.request
import re
from urllib.request import urlretrieve
import ssl
import os,sys


# headers=r'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
# "Cookie":"vote=1; __utmz=5621947.1510501763.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); forum_post_last_read_at=%222018-01-17T15%3A40%3A00.406%2B01%3A00%22; country=CN; yande.re=L0VFN1BYMWQwQjRndDZSM0ZtRGdqbTNtTHVjaWNUay9lcjAvZjZEeWdQMjEwMVQ0MnI4TXJWZHliR3kxV3dSZ1M1UlA0aWVtVVc4aWZhcjhCRjV4MlpxOFVMNWloSmVRaXluYnhZVXdPbFFveGNVSmVzZU85YTJ5V1NGNzdOai9TYUlOUGkraFpyaFN5KzlWN200WGI4OXhHMFluWGhVWE1SK3cyMnQ1eWtwaGdkSnlBdUYvUUxTM3hKMnlrU25PLS10Rm1LcHZEaWIveTYxbXlKbWFKOHhRPT0%3D--83e892db4fad6c1dad44e5ee766f8874694128fa; __utma=5621947.546481103.1510501763.1516197598.1516200022.7; __utmc=5621947; __utmt=1; __utmb=5621947.1.10.1516200022",
"Host":"yande.re",
# "If-None-Match":"W/\"ad59bebdf912e30db229970fe4c3d277\"",
# "Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False

def callbackfunc(blocknum, blocksize, totalsize):
     # 回调函数
     # @blocknum: 已经下载的数据块
     # @blocksize: 数据块的大小
     # @totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
         percent = 100
    print ("%.2f%%"% percent)

def download_page(url):
	request = urllib.request.Request(url) 
	response = urllib.request.urlopen(request)
	data = response.read() 
	data = data.decode('utf-8') 
	print(data)
	return data

def get_image(html):
	regx=r'src="(.+?\.jpg)"'
	# regx=r'[a-z|0-9|A-Z][\S]*.jpg'
	partten=re.compile(regx)
	get_img=re.findall(partten,html)
	# print(repr(html))
	num=1
	mkdir('img')
	local=sys.path[0]+r'\img\\'
	# print(local)
	for img in get_img:
		try:
			print('正在下载第%s张图片'%num)
			mlocal=local+str(num)+'.jpg'
			urllib.request.urlretrieve(img,mlocal,callbackfunc)
			num+=1
		except Exception as e:
			print (format(e))
			continue

try:
	# url=r'http://tieba.baidu.com/p/2460150866'
	url=r'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%99%BD%E4%B8%9D&oq=%E7%99%BD%E4%B8%9D&rsp=-1'
	html=download_page(url)
	get_image(html)
except Exception as e:
	print (format(e))


