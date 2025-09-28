'''
Implemente un programa que permita imprimir y contar los números múltiplos de 3 que
hay entre 1 y 100
'''
contador=0
for i in range(1,101):
    if i%3==0:
        contador+=1
        print(i)
print('Son',contador,'numeros')
