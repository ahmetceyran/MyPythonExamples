def basamaklar(sayi):
    binler,kalan=divmod(sayi,1000)
    yüzler,kalan=divmod(kalan,100)
    onlar,kalan=divmod(kalan,10)
    birler,kalan=divmod(kalan,1)
    return binler,yüzler,onlar,birler
x=basamaklar(1534)
print(x)
