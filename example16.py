ksayi=int(input("bir sayı giriniz:"))
k=0
for i in range (2,ksayi+1):
    if ksayi%i==0:
        k=k+1

if k==1:
    print("sayı asaldır")
else:
    print("sayı asal değildir")
