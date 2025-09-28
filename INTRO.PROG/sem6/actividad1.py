num=int(input('Escribe el numero:'))
sumdig=0
mayor=0
while num <=9999 and num>=1000:
    u=num%100
    d=u//10
    sumdig+=d
    if num>mayor:
        mayor=num
    num=int(input('Escribe el numero:'))

print(sumdig)
print(mayor)