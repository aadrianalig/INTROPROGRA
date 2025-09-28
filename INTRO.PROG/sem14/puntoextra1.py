'''2. Se tiene una estructura de datos que representa el número de productos vendidos en 3 tiendas durante 3 días (representación de una tienda y un día).
Ejemplo:
ventas = [[5, 3, 4],
         [2, 7, 1],
        [6, 2, 5]]

Escribe un programa que:
Calcule la suma total de productos vendidos.
Muestre el resultado de las ventas para cada tienda.
La información se genera en forma aleatoria (productos vendidos) entre 25 y 85.
'''
import random
def matriz():
    matriz=[]
    for i in range(3):
        fila=[]
        for j in range(3):
            elemento=random.randint(25,85)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz


def sumaTotal(matriz):
    sumatoria=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            sumatoria+=matriz[i][j]
    print('La suma total es de:',sumatoria)

def ventasTienda(matriz):
    for i in range(len(matriz)):
        sumaFila=0
        for j in range(len(matriz[i])):
            sumaFila+=matriz[i][j]
        print('La suma de la tienda',i+1,'es',sumaFila)

if __name__=='__main__':
    print('----MATRIZ----')
    a=matriz()
    sumaTotal(a)
    print('------------')
    ventasTienda(a)