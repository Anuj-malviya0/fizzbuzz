import time
y = float(input("enter the delay in seconds "))
x = int(input("enter the timer"))
x = x + 1
for i in range(1,x):
    print(i)
    time.sleep(y)
print("_" * 80)    
print(" {:^75}".format ("TIME COMPLETED"))
print("_" * 80)
a = input()
