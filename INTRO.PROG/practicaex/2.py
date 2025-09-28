'''🧪 Ejercicio 2: Buscar Número
Crea una matriz de NxM con valores aleatorios entre 15 y 45. Luego:
Pide un número por consola.
Devuelve la posición (fila, columna) donde aparece por primera vez.
Si no se encuentra, imprime 0.'''
import random
def matriz(n,m):
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(m):
            elemento=random.randint(15,45)
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
        print(fila)
    return matriz

def busquedaNum(matriz,target):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==target:
                print(target,'esta en la posicion',i+1,j+1)
                return (i,j)
    else:
        print('no')
        return False        
if __name__=='__main__':
    a=matriz(3,3)
    busquedaNum(a,20)