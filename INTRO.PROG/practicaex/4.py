'''🧪 Ejercicio 4: Mayor por Columna
Dada una matriz de 4x3 ingresada por consola, crea una lista con el valor máximo de cada columna.'''
import random
def matriz():
    matriz=[]
    for i in range(3):
        fila=[]
        for j in range(4):
            elemento=random.randint(1,5)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def maxColumna(matriz):
    for j in range(len(matriz[0])):
        mayor=matriz[0][j]
        for i in range(len(matriz)):
            if matriz[i][j]>mayor:
                mayor=matriz[i][j]
        print('El mayor de la columna',j+1,'es',mayor)

if __name__=='__main__':
    a=matriz()
    maxColumna(a)
