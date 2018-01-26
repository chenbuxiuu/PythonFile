import urllib
import urllib.request
import re
from urllib.request import urlretrieve
import ssl
import os,sys
import threading
from time import ctime,sleep


# headers=r'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
headers={
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
     "referer":"https://image.baidu.com"
    }

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
    global count
    thread = threading.current_thread()
    n=float(thread.getName())
    n=int(n)
    print('正在下载第%d张图片'%n,end=',')
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
    	percent = 100
    print('下载进度为%.2f%%'%(percent))





def download_page(url):
	request = urllib.request.Request(url) 
	response = urllib.request.urlopen(request)
	data = response.read() 
	data = data.decode('utf-8') 
	# print(data)
	return data


def save_img(img,local,callbackfunc):
	
	urllib.request.urlretrieve(img,local,callbackfunc)
	

def get_image(html,page,keyword):
	p=re.compile("thumbURL.*?\.jpg")
	get_img=p.findall(html)
	# print(repr(html))
	num=1
	mkdir(keyword)
	local=sys.path[0]+'\\'+keyword+'\\'
	# print(local)
	download_threads=[]
	for img in get_img:
		try:
			img=img.replace("thumbURL\":\"","")
			n=num+(page-1)*30
			# print('正在下载第%d张图片'%n)
			# print(img)
			mlocal=local+str(n)+'.jpg'
			# urllib.request.urlretrieve(img,mlocal,callbackfunc)
			t = threading.Thread(target=save_img, name=str(n),args=(img,mlocal,callbackfunc))
			download_threads.append(t)
			num+=1
		except Exception as e:
			print (format(e))
			continue

	for t in download_threads:
		t.start()
	t.join()

try:
	# url=r'http://tieba.baidu.com/p/2460150866'
	url1=r'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pageNum}&rn=30&gsm=1e00000000001e&1490169411926="'
	mkeyword='coser'
	keyword=urllib.parse.quote(mkeyword,"utf-8")
	n=0
	while(n<30*1):
		n+=30
		url=url1.format(word=keyword,pageNum=str(n))
		html=download_page(url)
		get_image(html,n/30,mkeyword)
except Exception as e:
	print (format(e))


