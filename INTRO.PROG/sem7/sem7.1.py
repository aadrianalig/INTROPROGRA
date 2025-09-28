#Definir parámetros
def f(x):
    return 3*x**2+5*x+10 #Definir función
a=f(6) #Función en Z=f(x)
print(f(5)) #print()

def esPar(x):
    if x%2==0:
        return True
    else:
        return False
print(esPar(3))

def f(x,positivo):
    if positivo:
        return x**2
    else:
        return x**3
print(f(2,False))
