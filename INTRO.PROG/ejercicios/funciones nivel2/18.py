'''Solicita un número del 0 al 9999 e indica cuántas cifras tiene.
'''

num=int(input('Escribre un numero: '))
def cantidadCifras(num):
    contador=0
    while num!=0:
        num=num//10
        contador+=1
    return contador
print(cantidadCifras(num))
        
        