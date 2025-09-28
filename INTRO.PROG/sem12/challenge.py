
'''Problema 2'''
def busquedaTarget(lista,target): 
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i>j:
                if lista[i]+lista[j]==target:
                    return j,i
print(busquedaTarget([3,2,4],6))

def sumaLista(digits):
    suma=0
    for i in range(0,len(digits)):
        x=digits[i]*10**(len(digits)-i-1)
        suma+=x
    suma=suma+1
    nuevaLista=[]
    for i in range(0, len(digits)):
        nuevaLista.append(((suma// 10**(len(digits)-(i+1)))%10))
    return nuevaLista
print(sumaLista([1,2,3]))
