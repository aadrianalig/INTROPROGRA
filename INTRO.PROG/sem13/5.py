'''Dada una matriz de 4x3 con números enteros ingresadas por consola, escribe una
función que devuelva una lista con el valor máximo de cada columna
'''

def main():
    matriz = []
    for i in range(4):
        fila = []
        for j in range(3):
            elemento = int(input(f'Escribe un número para la fila {i}, columna {j}: '))
            fila.append(elemento)
        matriz.append(fila)

    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)

    maximos = maximoColumna(matriz)
    print("\nMáximo de cada columna:")
    print(maximos)

def maximoColumna(matriz):
    maximos = []
    for j in range(3):  # Recorrer columnas
        max_val = matriz[0][j]
        for i in range(4):  # Recorrer filas
            if matriz[i][j] > max_val:
                max_val = matriz[i][j]
        maximos.append(max_val)
    return maximos

# Llamamos a main para ejecutar todo
main()
