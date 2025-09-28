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

n=10
lista=[]
for i in range(n):
    x=int(input('Escribe un valor para la lista: '))
    lista.append(x)

print(maxValor(lista))
print(buscarMaximo(lista))