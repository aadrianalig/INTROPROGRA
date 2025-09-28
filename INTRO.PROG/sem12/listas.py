n=10
lista=[]
for i in range(n):
    x=int(input('Escribe un valor para la lista: '))
    lista.insert(0,x)
print(lista)

n=10
lista2=[]
for i in range(n):
    x=int(input('Escribe un valor para la lista: '))
    lista2.insert(0,x)
print(lista2)

suma=0
for i in range(len(lista)):
    suma+=lista[i]
print('el promedio es',suma/n)