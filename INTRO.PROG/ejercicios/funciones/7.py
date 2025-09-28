'''
Escriba una función con la siguiente definición:
imprimirMatriz(n)
Lo que hará esta función será imprimir una matriz cuadrada de dimensiones n x n.
Considere que cada elemento de la matriz será el carácter asterisco (*)
'''
n=int(input('Escribe un numero: '))
def imprimirMatriz(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print('😎',end='\t')
        print()
imprimirMatriz(n)