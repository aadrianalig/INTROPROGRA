contador=0
contadorcalor=0
contadorfrio=0
suma=0
temp=int(input('Escribe el numero: '))


while temp>0:
     suma+=temp
     contador+=1
     if temp>23:
        contadorcalor+=1
     elif 5<=temp<=10:
        contadorfrio+=1
     temp=int(input('Escribe el numero: '))
promedio=suma/contador
print(contadorfrio)
print(contadorcalor)
print(promedio)