from quadratic import quadratic
from HigherOrderFunction import PositiveIntegerAdd
a=input("a=")
a=float(a)
b=input("b=")
b=float(b)
c=input("c=")
c=float(c)

quadratic(a,b,c)

x=-1
y=2
print("abs(%d)+abs(%d)="%(x,y),PositiveIntegerAdd(x,y,abs))
