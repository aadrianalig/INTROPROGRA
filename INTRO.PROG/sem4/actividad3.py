sumaNotas=0
cantidadNotas=0
nota=int(input('Escribe la nota: '))
if nota>20 and nota<=0:
    nota=int(input('Escribe nuevamente la nota: '))
respuesta=input('Desea escribir más notas?')
while respuesta =='si':
     nota=int(input('Escribe la nota: '))
     sumaNotas+=nota
     cantidadNotas+=1
     respuesta=input('Desea escribir más notas?')
promedio=sumaNotas/cantidadNotas
print(promedio)

#Promedios
if promedio<11:
     print('Desaprobado')
elif promedio>=11 and promedio<13:
     print('Nota regular')
elif promedio>=14 and promedio<17:
     print('Buen trabajo')
elif promedio>=17 and promedio<20:
     print('Excelente desempeño')
else:
     print('Error')

     