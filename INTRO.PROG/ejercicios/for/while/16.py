'''
Implemente un programa que permita imprimir en pantalla el siguiente patrón tomando
como entrada un valor “n” que determina la cantidad de líneas que se imprimirán (el
ejemplo muestra lo que debe mostrarse para para n = 3  3 líneas):

***
*****
*********
'''
for i in range(1,4):
    for j in range(1,3+(2**i)):
        print('*' ,end='')
    print()