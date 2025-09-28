def numeroDigitos(num):
    cont=0
    while num!=0:
        num=num//10
        cont+=1
    return cont
#print(numeroDigitos(12345333))

def esPrimo(n):
    if n <= 1:
        return False  # 0 y 1 no son primos

    # Verifica si algún número entre 2 y n-1 divide exactamente a n
    for i in range(2, n):
        if n % i == 0:
            return False  # Tiene un divisor, no es primo
    return True
print(esPrimo(7))


def numeroPrimo(n):
    divisores=0
    for i in range(1,n+1):
        if n%i==0:
            divisores+=1
    if divisores!=2:
        return False
    else:
        return True
print(numeroPrimo())

