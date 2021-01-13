#defining a function 
def fizzBuzz(n):
    #checking that n is multiple of both 3 & 5 or not 
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    #checking that n is multiple of 3 or not 
    elif n % 3 == 0 and n % 5 != 0:
         print("Fizz")
    #checking that n is multiple of 5 or not 
    elif n % 5 == 0 and n % 3 != 0:
        print("Buzz")
    #printing the number as it is
    else:
        print(n)
#running function in side for loop  
for n in range(1,101):
     a = fizzBuzz(n)
 
