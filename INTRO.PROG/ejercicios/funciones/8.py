'''
Un número es capicúa si se lee igual de izquierda a derecha y de derecha a izquierda. Por
ejemplo: 232 es capicúa, pero 123 no lo es. Desarrolle un programa que imprima un
mensaje diciendo si un número es capicúa o no. Para ello programe dos funciones con las
siguientes definiciones:
● invertir(n)
● es_palindromo(n)
La función es_palindromo recibirá como argumento un número entero n y luego lo enviará
a la función inversa(n), la cual retornará el número invertido. Luego comparará ambos
números, el original y el invertido, e imprimirá un mensaje diciendo si el número cumple o
no con ser capicúa
'''
num=int(input('Escribe el numero: '))
def esPalindromo(num): 
    if num//100 == num%10:
        print(True)
    else: 
        print(False)
    
def invertir(num):
    inicio= num//100 
    fin= num%10
    if str(inicio)+str((num%100)//10)+str(fin)==num:
        return True        
    else:
        return False
esPalindromo(num)
invertir(num)