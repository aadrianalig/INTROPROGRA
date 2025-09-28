'''Solicita dos números e indica si el primero es múltiplo del segundo.
'''

a=int(input('Escribre un numero: '))
b=int(input('Escribre otro numero: '))
def multiploDelOtro(a,b):
    if a%b==0:
        print(a,'es multiplo de',b)
    elif b%a==0:
        print(b,'es multiplo de',a)
    else:
        print('no tienen ninguna relacion')
multiploDelOtro()
    