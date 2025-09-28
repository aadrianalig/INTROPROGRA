numero=int(input('Escribe el número:'))
r=int(input('Escribe el rango:'))
for i in range(r):
    if i%10==0:
        print('---------------')

    print(i,'*',numero,'-----',i*numero)