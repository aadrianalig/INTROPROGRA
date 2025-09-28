#los elementos más pesados van más arriba
def ordenarBurbnuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if lista[i]<lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

edades=[45,25,64,12,17,49]
listaOrdenada=ordenarBurbnuja(edades)
print(listaOrdenada)