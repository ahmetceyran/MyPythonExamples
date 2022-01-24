def ozFakt (n):
    if n==0:
        return 1
    else:
        return n*ozFakt(n-1)

a = int(input("Öz faktoriyeli hesaplanacak sayiyi giriniz : "))
print(ozFakt(a))
