'''🧪 Ejercicio 6: Promedio por Columna y cuántos están sobre el promedio
Dada una matriz de NxM con valores aleatorios entre 10 y 50:
Calcula el promedio de cada columna.
Para cada columna, muestra cuántos elementos están por encima del promedio de esa columna.'''

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

def promedioColumna(matriz):
    for j in range(len(matriz[0])):
        sumaColumna = 0
        for i in range(len(matriz)):
            sumaColumna += matriz[i][j]
        promedio = sumaColumna / len(matriz)
        print('Promedio de la columna', j+1, '--->', promedio)

        contadorColumna = 0
        for i in range(len(matriz)):
            if matriz[i][j] > promedio:
                contadorColumna += 1
        print('Hay', contadorColumna, 'elementos encima del promedio en la columna', j+1)


if __name__=='__main__':
    a=matriz(3,3)
    promedioColumna(a)