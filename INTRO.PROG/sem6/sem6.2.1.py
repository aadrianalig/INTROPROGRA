respuesta=input('Desea ingresar más numero?: ')

while respuesta == 'si':
    print('Cuantos numeros desea ingresar: ')
    n=int(input())
    print('Ingresa',n,'numeros')
    suma=0
    mayor=0
    menor=10000000000
    for i in range(1,n+1):
        print('Ingresa el numero ',i)
        m=int(input())
        suma+=m
        if m>mayor:
            mayor=m
        if m<menor:
            menor=m
    print('El numero mayor es:',mayor)
    print('El numero menor es:',menor)
    print('La suma es:',suma)
    print('El promedio es:',suma/n)
    respuesta=input('Desea ingresar más numero?:  ')
