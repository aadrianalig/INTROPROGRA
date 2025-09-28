'''
Solicita tres calificaciones y muestra el promedio.'''

def promedioTres(a,b,c):
    promedio=(a+b+c)/3
    return promedio
a=int(input('Escribre un numero: '))
b=int(input('Escribre otro numero: '))
c=int(input('Escribre otro numero: '))
print(promedioTres(a,b,c))