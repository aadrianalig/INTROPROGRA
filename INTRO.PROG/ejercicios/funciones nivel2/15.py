'''
Determina si un año ingresado es bisiesto.
'''
def verificadorAno(anio):
    if anio%4==0 or anio%400==0:
        print('Es bisiesto')
    else:
        print('No es bisiesto')
verificadorAno(2020)