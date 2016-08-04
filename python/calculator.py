loop=1
opt=0
while loop==1:
    print("Enter your choice:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit")
    opt=int(input())
    if opt==1:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        print(a+b)
    elif opt==2:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        print(a-b)
    elif opt==3:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        print(a*b)
    elif opt==4:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        print(a//b)
    elif opt==5:
        break
    else:
        print("Enter valid option!")
