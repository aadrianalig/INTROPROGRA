'''
Implemente un programa que determine el conjunto de números que hay entre la unidad y
un determinado número introducido por el teclado. Tomando en cuenta el grupo de
números mencionado, su programa debe imprimir, sumar y contar los números del grupo
que son a la vez múltiplos de 2 y de 3.
'''
contador=0
condicion=0
num=int(input('Escribe un numero: '))
if num<=1:
    print('No se puede ejecutar el programa')
else:
    for i in range(1,num+1):
        contador+=1
        if i%2==0 and i%3==0:
            condicion+=1
        print(i)
    print('Son',contador,'numeros y solo',condicion,'cumplen la condicion')