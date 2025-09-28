num=int(input('Escribe el numero: '))
promedio=0
contador=0
sum=0

while num<100:
    contador+=1
    sum+=num
    promedio=sum/contador
    num=int(input('Escribe el numero: '))
    if num>promedio:
        print('no da')

