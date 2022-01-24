N = int (input("pozitif bir tam sayı giriniz: "))
x = 2
for x in range (x,N+1):
    i = 2
    for i in range (i,x):
        if x % i == 0:
            break
        i += 1
    else:
        print (x)
    x += 1
    
