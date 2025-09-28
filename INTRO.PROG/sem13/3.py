'''Escribe una función que reciba una lista de listas cuadrada (misma cantidad de filas
y columnas) y retorne su matriz transpuesta
'''
import random
def main(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = random.randint(15, 20)
            fila.append(elemento)
        matriz.append(fila)
        print("Matriz original:")
    for fila in matriz:
        print(fila)

    trans = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(matriz[j][i]) 
        trans.append(fila)

    print("\nMatriz transpuesta:")
    for fila in trans:
        print(fila)
    return trans

if __name__=='__main__':
    main(4)