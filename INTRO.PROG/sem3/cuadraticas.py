
a=int(input('Escribe el valor de A: '))
b=int(input('Escribe el valor de B: '))
c=int(input('Escribe el valor de C: '))
#Discriminante
Discri=b*b-4*a*c

if Discri>0:
    Raiz1=(-1*b-(b**2-4*a*c)**1/2)/(2*a)
    Raiz2=(-1*b+(b**2-4*a*c)**1/2)/(2*a)
    print('Tiene raices reales y son',Raiz1,'y',Raiz2)
if Discri==0:
    Raiz=(-1*b-(b**2-4*a*c)**1/2)/(2*a)
    print('Solo tiene una raiz real y es: ', Raiz)
if Discri<0:
    print('La ecuacion no tiene raices reales')

