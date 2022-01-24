from math import sqrt
a=int(input("a değerini giriniz: "))
b=int(input("b değerini giriniz: "))
c=int(input("c değerini giriniz: "))
d=b*b-4*a*c
if d<0:
    print("kökler sanal")
else:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print(x1,x2)
    
