def max(a,b):
    if a>b:
        return a
    else:
        return b

'''
a=int(input('Escribe un numero: '))
b=int(input('Escribe otro numero: '))
c=int(input('Escribe otro numero: '))
'''
#print('El mayor es',max(max(a,b),c))

def vocales(caracter):
    if caracter =='a' or 'A':
        return True
    elif caracter =='e' or 'E':
        return True
    elif caracter =='i' or 'I':
        return True
    elif caracter =='o' or 'O':
        return True
    elif caracter =='u' or 'U':
        return True
    else:
        return False
print(vocales('p'))

