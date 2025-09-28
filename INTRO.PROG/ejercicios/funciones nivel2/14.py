'''Pide una contraseña y verifica si coincide con una almacenada.'''
contrasenia=input('Establece una contrasenia: ')
intento=input('Escribe la contrasenia: ')
def verificadorContrasenia(intento):
    while intento!=contrasenia:
        print('\contrasenia incorrecta/')
        intento=input('Escribe la contrasenia: ')
    print('---zContrasenia correcta---')
verificadorContrasenia(intento)