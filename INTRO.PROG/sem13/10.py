import random
def masLarga(lista):
    idx=0
    for i in range(len(lista)):
        if len(lista[i])>len(lista[idx]):
            idx=i
    return idx
