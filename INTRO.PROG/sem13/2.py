'''Dada una matriz de tamaño ingresado por el usuario y valores generador aleatoris
entre 15 y 45, implemente una función que reciba un número, la matriz y devuelva
la posición (fila, columna) donde se encuentra por primera vez. Si no se encuentra,
debe retornar 0
'''

import random

def main(n,m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            elemento = random.randint(15, 45)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    numeroComprobar = int(input('Escribe el número a buscar: '))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numeroComprobar:
                print(f"Número encontrado en la posición: fila {i+1}, columna {j+1}")
                return
    print(0)

if __name__=='__main__':
    n=5
    m=5
    main(n,m)
