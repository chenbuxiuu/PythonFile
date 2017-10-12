from functools import reduce
import math
def normalize(name):
    return name.lower().capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
    t=[c for c in s if c != '.']
    return reduce(lambda x,y : x * 10 + y,map(lambda x :d[x],t))

def str2float(s):
    t=char2num(s)
    index=s.find('.')
    if index==-1:
        return t
    else:
        divisor=pow(10,len(s)-1-index)
        t=t/divisor
        return t
print(str2float('12345.567'))
