'''Pide un número n y muestra la suma de los números de 1 a n.
'''
def sumatoria(n):
    suma=0
    for i in range(1,n+1):
        suma+=i
    print(suma)
sumatoria(4)