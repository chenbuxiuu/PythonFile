import os
a=[x * x for x in range(1, 11) if x % 2 == 0]
print(a)
b=[m + n for m in 'ABC' for n in 'XYZ']
print(b)
f=[d for d in os.listdir('.')]
print(f)
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
     print(k, '=', v)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() if isinstance(s,str) else s for s in L1]
print(L2)
t=[s for s in '123.456']
print(t)
