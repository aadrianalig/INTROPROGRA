suma=0
num=int(input('Escribe el numero: '))
while num!=0:
     num=int(input('Escribe el numero: '))
     suma+=num%10
print(suma)

'''
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


print(promedio)'''