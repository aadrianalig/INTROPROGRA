'''Crea un programa que, dada una matriz de NxM, donde ambos valores son
ingresados por el usuario, luego, genere los valores en forma aleatoria, a
continuación, ingrese un número n y cuente cuántas veces aparece ese número en
toda la matriz'''

import random
def matriz(n,m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            elemento = random.randint(15, 45)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def numeroCompation(matriz,numeroComprobar):
    #numeroComprobar = int(input('Escribe el número a buscar: '))
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numeroComprobar:
                contador+=1
    print('Se han encontrado',contador,'veces el numero ingresado')

if __name__=='__main__':
    n=int(input('De cuantas filas quieres que sea la matriz: '))
    m=int(input('De cuantas columnas quieres que sea la matriz: '))
    a=matriz(n,m)
    num=int(input('Escribe el numero a comprobar: '))
    numeroCompation(a,num)