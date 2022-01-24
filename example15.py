sayi=int(input("Faktöriyel'i alınacak sayıyı giriniz: "))
faktoriyel=1
if(int(sayi) < 0):
    print("Yanlış sayi girişi yaptınız....")
else:
    i=1
    while i<=sayi:
        faktoriyel=faktoriyel*i
        i=i+1

print(faktoriyel)
