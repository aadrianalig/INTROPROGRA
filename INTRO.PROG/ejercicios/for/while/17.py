'''
Implemente un programa que lea desde el teclado una cadena de caracteres, un valor “n”
que representa el orden de una matriz y permita mostrar el siguiente patrón en pantalla
(se muestran resultados para n = 3  matriz de 3 x 3).
'''
n=int(input('Escribe un numero: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('hola',end='\t')
    print()