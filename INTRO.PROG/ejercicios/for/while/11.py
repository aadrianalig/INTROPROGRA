'''
Implemente un programa que imprima los números del 1 al 100 y calcule la suma de todos
los números para por un lado (suma par) y por otro lado la de los impares (suma impar).
'''
contadorPar=0
contadorImpar=0
for i in range(101):
    if i%2==0:
        contadorPar+=i
    else:
        contadorImpar+=i
print('La suma par es:',contadorPar,'y la suma impar es',contadorImpar)
