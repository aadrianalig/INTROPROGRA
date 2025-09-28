def crearListaNombres(n):
    lista=[]
    for i in range(n):
        n=input(f'Escribe el nombre:{i+1}')
        lista.append(n)
    print(lista)
    
    return lista

def buscarPersonas(asistentes,nombres):
    for i in range(len(asistentes)):
        print('asistente',i,'es',nombres)

if __name__=='___main__':
    n=int(input('Cantidad de nombnre?: '))
    nombre = crearListaNombres(n)