#columna major

def buscarColumnaMayor(matriz):
    for j in range(len(matriz[0])):
        columna=[]
        for i in range(len(matriz)):
            columna.append(matriz[i][j])
        print(columna)

def buscarFila(matriz):
    for i in range(len(matriz)):
        fila=matriz[i]
        print(fila)
    