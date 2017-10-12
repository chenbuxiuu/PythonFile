# -*- coding: utf-8 -*-
d={'A':0,'B':1,'C':2}
print(d)
print(d['A'])
for i in d:
    print("%s,%d"%(i,d[i]))
d['D']=4
for i in d:
    print("%s,%d"%(i,d[i]))
d.pop('A')
for i in d:
    print("%s,%d"%(i,d[i]))
print(d.get('A',-1))
print(d.get('C',-1))
