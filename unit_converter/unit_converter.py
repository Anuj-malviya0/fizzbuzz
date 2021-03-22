#writing all the available conversions
print('''
    \t\t\tAvailable conversions\nm(meter) to cm(centimeter),km(kilo meter)mm(mili meter),mile,inch
cm to m,km,mm,mile,inch

km to cm,m,mm,mile,inch

mile to m,cm,km,mm,inch

inch to m,cm,km,mm,mile
    ''')
#Accepting the input unit
iunit = str(input("Enter the unit from which want to convert "))
#Accepting the output unit
ounit = str(input("Enter the unit  in which want to convert "))
#checking the input unit and output unit and creating out put accordint to it 
#-----------------------------------m---------------------------------------
if iunit == "m":
    a = float(input("Enter the digit "))
    if ounit == "cm":
        print(a * 100)
    elif ounit == "km":
        print(a /1000)
    elif ounit == "mm":
        print(a * 1000)
    elif ounit == "mile":
        print(a / 1609)
    elif ounit == "inch":
        print(a * 39.37)
#------------------------------------cm----------------------------------------
elif iunit == "cm":
    a = float(input("Enter the digit "))
    if ounit == "m":
        print(a / 100)
    elif ounit == "km":
        print(a /100000)
    elif ounit == "mm":
        print(a * 10)
    elif ounit == "mile":
        print(a / 160934)
    elif ounit == "inch":
        print(a /2.54)
#----------------------------------------km---------------------------------------
elif iunit == "km":
    a = float(input("Enter the digit "))
    if ounit == "m":
        print(a * 1000)
    elif ounit == "cm":
        print(a * 100000)
    elif ounit == "mm":
        print(a * 1000000)
    elif ounit == "mile":
        print(a / 1.609)
    elif ounit == "inch":
        print(a * 39370)
#---------------------------------------mile-------------------------------------
elif iunit == "mile":
    a = float(input("Enter the digit "))
    if ounit == "m":
        print(a / 1609)
    elif ounit == "cm":
        print(a * 160934)
    elif ounit == "mm":
        print(a * 1609344)
    elif ounit == "km":
        print(a / 1.609)
    elif ounit == "inch":
        print(a * 63360 )
#---------------------------------------inch-------------------------------------
elif iunit == "inch":
    a = float(input("Enter the digit"))
    if ounit == "m":
        print(a / 39.37)
    elif ounit == "cm":
        print(a * 2.54)
    elif ounit == "mm":
        print(a * 1609344)
    elif ounit == "km":
        print(a / 39370)
    elif ounit == "mile":
        print(a / 63360)
#if none of the conditions meet returning else statement
else:
    print("you entered something wrong ")
#just a simple variable holding cmd (it close after the exceution program) 
l = input()
