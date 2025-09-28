'''Escriba un programa que calcule la potencia de un número a través del empleo
de una función recursiva. El programa debe solicitar primero el número que representa
la base y luego el número que representa al exponente. Al finalizar el programa, se
debe imprimir la potencia solicitada
'''

base=int(input('Esribe tu numero: '))
expo=int(input('Escribre la potencia: '))
def potencia(base,expo):
    if expo==0:
        return 1
    return base*potencia(base,expo-1)
print(potencia(base,expo))