def div(a):
    divA=0
    for i in range(1,a+1):
        if a%i==0:
            divA+=1
    if divA==2:
        return True
    else: 
        return False

def primo(a, b):
    if div(a)==True and div(b)==True:
        print(a,'y',b,'son primos')
    else:
         print(a,'y',b,'no son primos')
primo(2,3)

