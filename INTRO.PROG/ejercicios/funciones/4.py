'''
Implemente una función que reciba dos números enteros a y b, y calcule el resultado de ab
utilizando operaciones de multiplicación. Tome en cuenta que tanto a como b también
podrían tomar valores negativos
'''
def potencia(a, b):
    resultado = 1
    if b == 0:
        return 1
    elif b > 0:
        for i in range(b):
            resultado *= a
        return resultado
    else:  # b < 0
        for i in range(-b):
            resultado *= a
        return 1/resultado

a=int(input('Escribe tu numero: '))
b=int(input('Escribe tu numero: '))
print(potencia(a,b))

