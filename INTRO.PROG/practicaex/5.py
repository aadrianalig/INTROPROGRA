'''🧪 Ejercicio 5: Suma por Fila y Mayor Suma
Genera una matriz de 3x4 con valores aleatorios entre 1 y 20.
Luego:
Calcula la suma de cada fila y guárdala en una lista.
Muestra la fila con mayor suma total (índice).
'''
import random

def matriz():
    matriz=[]
    for i in range(3):
        fila=[]
        for j in range(4):
            elemento=random.randint(1,20)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def sumaFila(matriz):
    sumas=[]
    for i in range(len(matriz)):
        sumaFila=0
        for j in range(len(matriz[i])):
            sumaFila+=matriz[i][j]
        sumas.append(sumaFila)
    print('El lista con sumas por filas')
    print(sumas)

    mayor=sumas[0]
    filaMayor=0
    for i in range(len(sumas)):
        if sumas[i]>mayor:
            mayor=sumas[i]
            filaMayor=i
    print('La mayor es la fila',filaMayor+1)

if __name__=='__main__':
    a=matriz()
    sumaFila(a)
