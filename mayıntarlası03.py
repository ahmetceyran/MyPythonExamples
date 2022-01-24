import random

a=10
tarla=[[0 for x in range(a)] for y in range(a)]

for i in range(10):
    x=random.randint(0,9)
    y=random.randint(0,9)
    tarla[x][y]=1

for i in tarla:
    print(i)

satir=0
sutun=0
puan=0

while True:
    satir=int(input("Hangi satır: "))
    sutun=int(input("Hangi sutun: "))
    while tarla[satir][sutun]==2:
        print("Yeniden secim yapiniz (burasi acildi)")
        satir=int(input("Hangi satır: "))
        sutun=int(input("Hangi sutun: "))

    if tarla[satir][sutun]==1:
        print("Yandin,puan : ",puan)
        break
    tarla[satir][sutun] = 2
    puan+=10
