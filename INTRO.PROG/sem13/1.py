'''Genere una matriz de 4x4, con valores ingresados por el usuario (consola) a
continuación, cuente cuántos elementos son números pares en toda la matriz y
luego cuantos son números impares por cada fila
'''
#Llenado de matriz
def main():
    matriz=[]
    for i in range(4):
        fila = []
        for j in range(4):
            elemento= int(input('Ingresa Dato'))
            fila.append(elemento)
        matriz.append(fila)
    for fila in matriz:
       print(fila)

#Total de numeros pares de la matriz
    contPares=0
    for i in range(4):
        for j in range(4):
           if matriz[i][j]%2==0:
            contPares+=1
    print('Cantidad pares ',contPares)
#Total de numeros imprares por fila
    contImpares=[0,0,0,0]
    for i in range(4):
        for j in range(4):
           if matriz[i][j]%2 != 0:
            contImpares[i]+=1
    print('Canitdad de impares por fila ',contImpares)

    for i in range(len(contImpares)):
       print('Impares en fila',i,contImpares[i])

if __name__=='__main__':
    main()