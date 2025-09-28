forma=int(input('Que forma tiene tu poligono: 1. Triangulo, 2. Cuadrado, 3. Circulo     '))
if forma==1:
    altoTri=int(input('Escribe la altura del triangulo: '))
    baseTri=int(input('Escribe la base del triangulo: '))
    areaTriangulo=baseTri*altoTri/2
    print('el área del triangulo es: ',areaTriangulo)
if forma==2:
    ladoCua=int(input('Escribe cuanto es el lado del cuadrado: '))
    areaCua=ladoCua*ladoCua
    print('el área del cuadrado es: ',areaCua)
if forma==3:
    radio=int(input('Escribe el radio del circulo: '))
    area=3.14159*radio**2
    print('el área del circulo es: ',area)
else:
    print('------------número inválido---------------')