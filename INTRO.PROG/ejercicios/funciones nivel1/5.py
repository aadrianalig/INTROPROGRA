'''
Pide base y altura y muestra el área (área = base * altura / 2).
'''
def areaTriangulo(altura,base):
    Triangulo=altura*base/2
    return Triangulo
altura=int(input('Escribre la altura: '))
base=int(input('Escribre la base: '))
print(areaTriangulo(base,altura))