import random

h = 10
matrix=[[0 for x in range(h)] for y in range(h)]


for i in range(10):
     x = random.randint(0,9)
     y = random.randint(0,9)
     matrix[x][y] = 1

for i in matrix:
     print(i)

satir = 0
sutun = 0
puan = 0

while True:
     
     print("hangi satır")
     satir = int(input())
     print("hangi sutun")
     sutun = int(input())
     while matrix[satir][sutun] == 2:
          print("yeniden secim yapiniz (burasi acildi)")
          print("hangi satır")
          satir = int(input())
          print("hangi sutun")
          sutun = int(input())

     if matrix[satir][sutun] == 1:
          print("yandın. puan", puan)
          break
     matrix[satir][sutun] = 2
     puan+=10
