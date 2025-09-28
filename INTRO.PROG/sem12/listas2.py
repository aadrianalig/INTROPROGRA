def sumaElementos(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]

    return suma

n=10
lista=[]
for i in range(n):
    x=int(input('Escribe un valor para la lista: '))
    lista.insert(0,x)

print(sumaElementos(lista))