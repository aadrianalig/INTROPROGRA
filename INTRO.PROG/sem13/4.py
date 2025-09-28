'''Dada una matriz de 3x4, genera una nueva lista con la suma de los elementos de
cada fila'''
import random
def generar_matriz():
    matriz = []
    for i in range(3):
        fila = []
        for j in range(4):
            elemento = random.randint(1,5)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def nuevasListas(matriz):
    nlista = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        nlista.append(suma)
    print(nlista)

if __name__ == '__main__':
   a=generar_matriz()
   (nuevasListas(a))
    
