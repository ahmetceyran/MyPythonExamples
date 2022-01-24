import random

def fal(k,n):
    kalan=n%2
    if(k=="seviyor") and (kalan==1):
        print("seviyor")
    elif(k=="seviyor") and (kalan==0):
        print("sevmiyor")
    elif(k=="sevmiyor") and (kalan==1):
        print("sevmiyor")
    elif(k=="sevmiyor") and (kalan==0):
        print("seviyor")
    else:
        print("Hatalı giris yaptiniz!!")

def main():
    n=random.randint(0,100)
    k=input("Baslangic degerini giriniz(seviyor/sevmiyor) :")
    print("Yaprak sayısı: ",n)
    fal(k,n)
    x=input("Tekrar oynamak ister misiniz?[E/H]")
    if x=="E":
        main()
    else:
        return 0

main()
