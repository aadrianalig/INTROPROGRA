
def buscardor(lista,buscar):
    indices=[]
    for i in range(len(lista)):
        if lista[i]==buscar:
            indices.append(i)
            print('Lo que buscas esta en la posicion',i)
    return indices

def busquedaBinaria(lista,elemento):
    li=0
    ls=len(lista)
    medio=(li+ls)//2
    posx=-1
    while li <=ls:
        print('lo que estas buscando esta entre',li,ls)
        if lista[medio]==elemento:
            return medio
        
        if lista[medio]<elemento:
            print(lista[medio],'<',elemento)
            print('lo que buscas esta a la derecha')
            li=medio+1
        
        if lista[medio]>elemento:
            print(lista[medio],'>',elemento)
            print('lo que buscas esta a la izquierda')
            ls=medio-1

        medio=(li+ls)//2

    return posx
if __name__=='__main__':
    #print(buscardor([2,3,4,3,15],3))

    v=[2,3,4,8,17,25,38,43]
    idx=(busquedaBinaria(v,3))
    print('el elemento esta en la posicion',idx)