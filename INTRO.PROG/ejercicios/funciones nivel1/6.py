'''
Pide una cantidad de minutos y muestra cuántas horas y minutos representa.
'''
def conversionHoras(minuto):
    minuto=int(input('Escribe la cantidad de minutos: '))
    horas=minuto//60
    minutosRestantes=minuto%60
    print('Son',horas,'y',minutosRestantes,'minutos')
conversionHoras(min)