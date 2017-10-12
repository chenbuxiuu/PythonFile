# -*- coding: utf-8 -*-
s=input("height:")
height=float(s)
s=input("weight:")
weight=float(s)
bmi=weight/height/height
if bmi<18.5:
    print("过轻\n")
elif bmi>18.5 and bmi<25:
    print("正常\n")
else:
    print("肥胖\n")
print("bmi=%.2f"%bmi)
