'''
Implemente un programa que permita introducir dos valores A y B y realice el cálculo de la
expresión S. Muestre el resultado en pantalla.

1. Si A >= B
    S = 10 + 14 + 18 + … + 50

2. Si (A / B) <= 30
    S = A ^ 2 + B ^ 2

'''
a=int(input('Escribe un numero: '))
b=int(input('Escribe otro numero: '))
suma=0
if a>=b:
    for i in range(10,51):
        suma+=i
    print('El valor de S es:',suma)
elif a/b <=30:
    rpta=a**2+b**2
    print('El valor de S es de:',rpta)
else:
    print('No cumple ninguna condicion')