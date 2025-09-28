'''
Implemente un programa que permita introducir un número entero positivo a través del
teclado y e imprima en pantalla un mensaje indicando si es par o impar. El programa
deberá continuar leyendo hasta que le usuario ingrese un valor -1
'''
numero= int(input("Ingresa un número (-1 para salir): "))
while numero != -1:
    if numero % 2 == 0:
        print("El número", numero, "es PAR.")
    else:
        print("El número", numero, "es IMPAR.")
    numero = int(input("Ingresa un número entero positivo (-1 para salir): "))