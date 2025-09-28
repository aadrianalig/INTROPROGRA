'''Pide una nota del 0 al 20 y muestra si es ‘Aprobado’, ‘Desaprobado’ o ‘Nota inválida’.
'''
nota=int(input('Escribe tu nota: '))
def estadoNota(nota):
    if nota>10.5:
        print('Estas aprobado')
    else:
        print('Estas desaprobado')
estadoNota(nota)