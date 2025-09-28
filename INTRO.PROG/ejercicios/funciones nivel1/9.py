'''Solicita una temperatura en Celsius y muestra su equivalente en Fahrenheit.
'''
def celciusFahrenheit():
    temp=int(input('Escribe la temperatura en celcius:'))
    tempFah=temp*(9/5)+32
    return tempFah
print(celciusFahrenheit())