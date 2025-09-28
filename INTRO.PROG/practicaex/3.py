'''🧪 Ejercicio 3: Transpuesta
Pide al usuario una matriz cuadrada y retorna su transpuesta.'''
import random
def matriz(n):
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(n):
            elemento=random.randint(1,4)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def transpuesta(matriz):
    trans = []
    for j in range(len(matriz[0])):  
        fila = []
        for i in range(len(matriz)): 
            if 1>0:
                fila.append(matriz[i][j])
        trans.append(fila)
    print('Nueva matriz////')
    for fila in trans:
        print(fila)
    return trans


if __name__=='__main__':
    a=matriz(3)
    transpuesta(a)