'''Pide hora y minuto y muestra el formato AM/PM.
'''

hora = int(input('Escribe horas: '))
minuto = int(input('Escribe minutos: '))
def conversion24h12h(horas, minutos):
    if horas == 0:
        horas12 = 12
        periodo = 'AM'
    elif horas == 12:
        horas12 = 12
        periodo = 'PM'
    elif horas > 12:
        horas12 = horas - 12
        periodo = 'PM'
    else:
        horas12 = horas
        periodo = 'AM'
    print(f'{horas12}:{minutos:02d}{periodo}')
conversion24h12h(hora, minuto)
