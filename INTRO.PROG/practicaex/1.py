'''🧪 Ejercicio 1: Contar Pares e Impares por Fila
Crea una matriz de 4x4 ingresada por consola. Luego:
Cuenta cuántos elementos pares hay en total.
Cuenta cuántos impares hay por fila.'''

import random
def matriz(n,m):
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(m):
            elemento=random.randint(1,5)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def contadorPares(matriz):
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]%2==0:
                contador+=1
    print(contador)
    return contador

def imparesFila(matriz):
    sumaTotal=0
    for i in range(len(matriz)):
        contadorFila=0
        for j in range(len(matriz[i])):
            if matriz[i][j]%2!=0:
                contadorFila+=1
        print('Hay',contadorFila,'impares en la fila',i+1)
        sumaTotal+=contadorFila
    print('En total hay',sumaTotal,'impares')
    return sumaTotal

if __name__=='__main__':
    a=matriz(3,3)
    contadorPares(a)
    imparesFila(a)