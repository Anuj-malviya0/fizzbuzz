#defining a function 
def series(n):
    #creating two conunter variables
    a = 0
    b = 1    
    print(a)
    print(b)
    #implementing for loop
    for _ in range(2,n):
        '''shifting a to b,b to c '''
        c=a+b
        a=b
        b=c
        print(c)
#running function 
n = int(input('Enter how many numbers you want'))
series(n)
#palce holder variable (to hold the output window)
s = input()

