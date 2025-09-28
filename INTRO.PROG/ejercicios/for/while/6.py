'''
Implemente un programa que permita calcular e imprimir la suma siguiente: S = 1 + 4 + 7 + 10 + … + 52
'''
suma=0
for i in range(1,53,3):
    suma+=i
print(suma)