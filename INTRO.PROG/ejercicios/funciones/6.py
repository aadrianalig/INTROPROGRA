'''
Escriba un programa que tenga una función que retorne factorial de un número ingresado
por consola
'''
def factorial(n):
    producto=1
    for i in range(1,n+1):
        producto*=i
    print(producto)
(factorial(3))