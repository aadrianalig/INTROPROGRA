'''Pide peso (kg) y altura (m), calcula el IMC y muestra su clasificación.'''

peso=int(input('Escribe tu peso en kg: '))
altura=int(input('Escribe tu altura en m: '))
def calculoIMC(peso,altura):
    IMC=peso/altura**2
    return IMC
print(calculoIMC(peso,altura))