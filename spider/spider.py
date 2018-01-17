import urllib
import urllib.request
import re


# headers=r'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

def download_page(url):
	request = urllib.request.Request(url) 
	response = urllib.request.urlopen(request)
	data = response.read() 
	data = data.decode('utf-8') 
	print(data)
	return data

def get_image(html):
	regx=r'http://[\S]*\.png'
	partten=re.compile(regx)
	get_img=re.findall(partten,repr(html))
	print(repr(html))
	num=1
	for img in get_img:
		print(img)
		image=download_page(img)
		with open ('%s.jpg'%num,'wb') as fp:
			fp.write(image)
			num+=1
			print('正在下载第%s张图片'%num)

try:
	url=r'https://www.jianshu.com/p/696922f268df'
	html=download_page(url)
	get_image(html)
except Exception as e:
	print ( format(e))

# test=r'http://sjskhaka.jpg'
# partten=re.compile(test)
# result=re.match(partten,test)
# if result:
# 	print('match')
# else:
# 	print('error')

