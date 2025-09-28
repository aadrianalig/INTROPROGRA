'''Escriba un programa que solicite un número decimal y que calcule la suma de
los dígitos que lo componen. Al finalizar el programa debe imprimir la suma
'''
num=123
def sumaCifras(num):
    if num==0:
        return num  
    return num%10 + sumaCifras(num//10)
print(sumaCifras(num))

sumaCifras(num)