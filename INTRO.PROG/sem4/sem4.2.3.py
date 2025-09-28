'''
Implemente un programa que permita introducir dos números por teclado e imprimir los
números que hay entre ellos comenzando por el más pequeño. Muestre cuántos números
son, cuántos de ellos son pares y la suma de valores pares que hay en el grupo
mencionado.
'''
contadorPar=0
contadorImpar=0
numeroMenor=num=int(input('Escribe el numero: '))
numeroMayor=num2=int(input('Escribe el numero 2: '))
if num<num2:
    num=numeroMenor
else:
    num=numeroMayor
for i in range(numeroMenor,numeroMayor):
    if i%2==0:
        contadorPar+=i
    else:
        contadorImpar+=i
print(contadorPar,'y el otro contador es',contadorImpar)