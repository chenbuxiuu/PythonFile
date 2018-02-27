#!/usr/bin/env python3
f1=open('1.txt')
f2=open('2.txt')
r1=[]
r2=[]
# 从第1个文件提取源文件名
for line in f1.readlines():
	str='('
	str1 = line[0:line.find(str)-1]
	str1=str1.lower()
	# print(str1)
	r1.append(str1)
# 从第2个文件提取源文件名
for line in f2.readlines():
	# print(line)
	str=' in '
	str1 = line[line.find(str) + 4:]
	str='('
	str1 = str1[0:str1.find(str)-1]
	# print(str1)
	r2.append(str1)

n1=len(r1)
n2=len(r2)
print(n1)
print(n2)


for i in range(n1):
	count=0
	for j in range(n2):
		if(r1[i]==r2[j]):
			break
		else:
			count+=1
	if count>=n2:
		print(r1[i])
print('-------------------------------------')
for i in range(n2):
	count=0
	for j in range(n1):
		if(r2[i]==r1[j]):
			break
		else:
			count+=1
	if count>=n1:
		print(r2[i])

