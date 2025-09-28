'''
Escriba una función que devuelva la media o promedio de dos números solicitados al
usuario
'''
def promedio(n):
    suma=0
    for i in range(1,n+1):
        x=int(input('Escribe tu numero: '))
        suma+=x
    return(suma/n)
print(promedio(3))