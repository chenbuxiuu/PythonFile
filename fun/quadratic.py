#ax^2 + bx + c = 0
import math
def quadratic(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print("%sx^2+%sx+%sc=0"%(str(a),str(b),str(c)))
        d=b*b-4*a*c
        if d>=0:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            # print("x1=",end='')
            # print(x1)
            # print("x2=",end='')
            # print(x2)
            print("x1=",x1)
            print("x2=",x2)
            return x1,x2
        else:
            print("unsolvable")
    else:
        print("input error")


