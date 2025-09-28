'''Escriba un programa que calcule la suma de los primeros “n” números a través
del empleo de una función recursiva. El programa debe solicitar primero el número “n”
y después de los cálculos imprimir la suma.
'''
def suma(n):
    if n==1:
        return 1
    return n + suma(n-1)
print(suma(10))