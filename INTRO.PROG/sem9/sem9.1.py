def fibonacciRecur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacciRecur(n-1)+fibonacciRecur(n-2)

def fibonacci():
    f1=0
    f2=1
    print(f1,end='\t')
    print(f2,end='\t')
    for i in range(0,10):
        print(f1+f2, end='\t')
        temp=f1
        f1=f2
        f2=temp+f2
    print()

if __name__=='__main__':
    fibonacci()
    fibonacciRecur(7)