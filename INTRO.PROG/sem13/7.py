'''Para una matriz cuadrada, escribe un programa que calcule y muestre la suma de
la diagonal principal'''
import random
def matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = random.randint(1,5)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def diagonalMatriz(matriz):
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                suma += matriz[i][j]
    print(suma)

if __name__=='__main__':
    n=int(input('De que tamanio quieres que sea la matriz cuadrada: '))
    a=matriz(n)
    diagonalMatriz(a)