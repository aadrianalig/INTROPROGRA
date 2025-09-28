'''
Implemente un programa que permita introducir un número entero positivo a través del
teclado y e imprima en pantalla un mensaje indicando si es par o impar. El programa
deberá continuar leyendo hasta que le usuario ingrese un valor -1
'''
num=int(input('Escribe el numero: '))
par=1
impar=0
if num==-1:
    print('Fin del programa')
else:
    if num%2==0:
        num=par
    else:
        num=impar
    while num==0:
            nuevoNum=int(input('Escribe el numero: '))
    print('el numero es par')