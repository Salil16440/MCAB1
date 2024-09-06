def revstring():
    a = input("Enter first name \n")
    b = input("Enter last name\n")
    c = a + " " + b
    print("String entered: ",c.capitalize()) #converts the first character of the string to capital
    print("Reversed order :",  b, a)
    print("Length of string :", len(c)) #counts the number of characters in a string, including whitespace

def typecon():
    a= input("Enter number: ")
    print("Datatype of entered number: ",type(a)) #shows the datatype of the number; eg: int
    print("Integer representation: ",int(a)) #no decimal point representaion; eg: 5
    print("Float representation: ", float(a)) #has a decimal point representaion; eg: 5.0
    print("Complex representation: ", complex(a)) #represents number in complex number format; eg: (5+0j)

def recarea():
    a=int(input("Enter length of rectangle\n"))
    b=int(input("Enter breadth of rectangle\n"))
    c=a*b
    print("Area: ", c)
    str(c)
    d=format(c, ".2f")
    print("Area with 2 decimal places: ",d)

def avg():
    a=[1,2,3,4]
    print("Average = ",(sum(a)/len(a)))


f=1
while(f==1):
    c=int(input("Choose your operation:\n1) Reverse a string\n2) Convert type\n3) Find area of a rectangle\n4) Find average\n5) Exit\n"))
    if c==1:
        revstring()

    elif c==2:
        typecon()

    elif c==3:
        recarea()

    elif c==4:
        avg()
    
    elif c==5:
        print("Exitting.....")
        f=0

    else:
        print("Invalid entry...try again...")

