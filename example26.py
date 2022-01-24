class ogrenci:
    isim="ali"
    yas=20
    birthdate=2002
    def goster(a):
        print("isim :",a.isim)
        print("yas :",a.yas)
        print("dogum tarihi :",a.birthdate)


ali=ogrenci()
ali.isim="Ali Veli"
ali.yas=18
ali.birthdate=2003
ali.goster()
