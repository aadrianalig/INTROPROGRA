'''
numeros del 1 al 1000 que sea multiplo de 13, 19 y que termine en 7
'''
for i in range(10001):
    if (i%13==0 and i%19==0) and i%10==7:
        print(i)
    