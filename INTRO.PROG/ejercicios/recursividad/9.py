'''Implemente una función recursiva que permita calcular el valor de la función
matemática F evaluada en ""x"", dadas las siguiente condiciones: F(0) es 4 y para todo
valor de ""x"" mayor que 0 se cumple que F(x) = 16 + F(x - 1).Su programa principal
debe solicitar al usuario el ingreso de x del teclado, realizar el llamado correspondiente
a la función recursiva y mostrar un mensaje con el resultado en pantalla
'''

def funcion(x):
    if x==0:
        return 4
    elif x>0:
        return funcion(x-1) + 16
    else:
        return False
print(funcion(-2))