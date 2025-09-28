'''
Implemente un programa que permita introducir dos números por teclado e imprimir los
números que hay entre ellos comenzando por el más pequeño. Muestre cuántos números
son, cuántos de ellos son pares y la suma de valores pares que hay en el grupo
mencionado.
'''

contadorpar=contador=0
suma=0
numeroMenor=num=int(input('Escribe el numero: '))
numeroMayor=num2=int(input('Escribe el numero 2: '))
if num>num2:
    mayor=num
    menor=num2
else:
    menor=num
    mayor=num2
for i in range(menor,mayor+1):
    contador+=1
    suma+=i
    if i%2==0:
        contadorpar+=1
print('Hay',contador,' numeros y la suma es ',suma,'y',contadorpar,'son pares')
