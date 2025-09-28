'''Solicita dos números y muestra cuál es mayor.
'''

a=int(input('Escribre un numero: '))
b=int(input('Escribre otro numero: '))
def mayorDos(a,b):
    if a>b:
        print('El mayor es',a)
    else:
        print('El mayor es',b)
mayorDos(a,b)