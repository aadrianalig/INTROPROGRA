num= 7526
suma=0

while (num!=0):
    u=num%10
    v=num//10
    num=v

    suma=suma+u
    print(u)

print(suma)