def buscarMenor(lista):
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]

    return menor

def ordenarLista(lista):
    listaOrdenada=[]
    while (len(lista)!=0):
        menor=buscarMenor(lista)
        listaOrdenada.append(menor)
        print('El elemento menor es',menor)
        lista.remove(menor)
    print(listaOrdenada)

    return listaOrdenada

if __name__=='__main__':
    a=[22,34,70,56]
    print(a)
    buscarMenor(a)
    ordenarLista(a)