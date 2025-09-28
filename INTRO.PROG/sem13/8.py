'''Dada una matriz, encuentra el índice de la fila cuya suma de elementos sea la
mayor.'''
import random
def matriz(n,m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            elemento = random.randint(1,5)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def filaMayor(matriz):
    mayor=0
    for i in range(len(matriz)):
        suma=0
        for j in range(len(matriz[i])):
            suma+=matriz[i][j]
        if mayor<suma:
            mayor=suma
            indice=i+1
    print('en la fila',indice,'y la suma es',mayor)

if __name__ == "__main__":
    n=int(input('De cuantas filas quieres que sea la matriz: '))
    m=int(input('De cuantas columnas quieres que sea la matriz: '))
    a=matriz(n,m)
    filaMayor(a)