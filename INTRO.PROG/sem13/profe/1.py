def crearLista(n):
    lista=[]
    for i in range(n):
        n=int(input(f'Escribe el numero:{i+1}'))
        lista.append(n)
    print(lista)
    
    return lista

def mayorElemento(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

def menorElemento(lista):
    menor=lista[i]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor

def promedioLista(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma/len(lista)

crearLista(3)
if __name__=='___main__':
    lista = crearLista(3)
    print(lista)
    print('el maximo es',mayorElemento(lista))
    print('el menor es',menorElemento(lista))
    print('el promedio es',promedioLista(lista))