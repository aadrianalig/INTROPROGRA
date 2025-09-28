numero=1
for i in range(1,11):
    for j in range(1,11):
        if numero%5==0:
            print('x',end='\t')
        else:
            print(numero,end='\t')
        numero+=1
    print() 