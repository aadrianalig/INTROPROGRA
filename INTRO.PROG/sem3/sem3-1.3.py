num1=int(input('escribe el 1er numero: '))
num2=int(input('escribe el 2do numero: '))
if num2 == 0:
    print('--------no se puede dividir--------')
else:
    div=num1/num2
    residuo= num1%num2
    if residuo == 0:
        print('division exacta, el numero es:',div)
    else:
        print('division inexata',div)
