'''
Implemente un programa que permita calcular e imprimir la suma siguiente: S = 50 + 48 + 46 + 44 + … + 20
''' 
suma=0
for i in range(20,51,2):
    suma+=i
print(suma)