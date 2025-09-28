'''
Escriba una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números que el usuario ingrese hasta que se digite cero. Luego
de leer dicho valor, mustre en pantalla el resultado final
'''
def sum():
    x = int(input('Escribe un número (0 para terminar): '))
    suma=0
    while x!=0:
        suma+=x
        x = int(input('Escribe un número (0 para terminar): '))
    print(suma)

def mult():
    x = int(input('Escribe un número (0 para terminar): '))
    producto=1
    while x!=0:
        producto*=x
        x = int(input('Escribe un número (0 para terminar): '))
    print(producto)

sum()
mult()