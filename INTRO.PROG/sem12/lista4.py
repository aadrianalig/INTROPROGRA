def buscarMaximo(lista):
    idxMaximos=[]
    maxIMO=maxValor(lista)
    for i in range(len(lista)):
        if lista[i]==maxIMO:
            idxMaximos.append(i)
    return idxMaximos

def maxValor(lista):
    max=0
    for i in range(len(lista)):
        if lista[i]>=max:
            max=lista[i]
    return max

lista=[34,78,32,24,78]
nombres = ["Ana", "Carlos", "Luis", "María", "Sofía"]
