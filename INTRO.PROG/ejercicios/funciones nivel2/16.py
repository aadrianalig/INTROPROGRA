'''Clasifica la edad como niño, adolescente, adulto o anciano.
'''
def clasificadorEdad(edad):
    if edad<15:
        print('Eres un ninio')
    elif 15<edad>=18:
        print('Eres un adolescente')
    else:
        print('Eres un anciano')
clasificadorEdad(18)