def fal(k,n):
    kalan=n%2
    if(k=="seviyor") and (kalan==1):
        print("sevmiyor")
    elif(k=="seviyor") and (kalan==0):
        print("seviyor")
    elif(k=="sevmiyor") and (kalan==1):
        print("seviyor")
    elif(k=="sevmiyor") and (kalan==0):
        print("sevmiyor")
    else:
        print("Hatalı giris yaptiniz!!")

def main():
    n=int(input("Yaprak sayısını giriniz :"))
    k=input("Baslangic degerini giriniz :")
    fal(k,n)
    x=input("Tekrar oynamak ister misiniz?[E/H]")
    if x=="E":
        main()
    else:
        return 0

main()
