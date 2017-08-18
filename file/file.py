with open('test.txt', 'w+') as f:
    for i in range(3):
        f.write('Hello, world!\n')
f=open('test.txt', 'r')
# print(f.read())

print(f.read(10))

# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

