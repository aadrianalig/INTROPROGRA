'''Dada una matriz (lista de listas) de cadenas generadas a partir del usuario, cuente
cuántas palabras en total comienzan con una vocal (mayúscula o minúscula)'''

def esVocal(letra):
    if letra.upper()=='A':
        return True
    if letra.upper()=='E':
        return True
    if letra.upper()=='I':
        return True
    if letra.upper()=='O':
        return True
    if letra.upper()=='U':
        return True
    

def contarInicioVocales(matriz):
    contador=0
    print(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            inicio=matriz[i][j][0]
            if esVocal(inicio):
                contador+=1
    return contador

if __name__=='__main__':
    nombres = [['ana','bruno','edgar'],
            ['andrea','beatriz','antonio']]
    print(contarInicioVocales(nombres))