def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def div(a,b):
    print(a//b)
loop=1
while loop==1:
    #Option
    print("Enter your option:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit")
    opt=int(input())
    if 1<=opt<5:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        if opt==1:
            add(a,b)
            loop==1
        elif opt==2:
            sub(a,b)
            loop==1
        elif opt==3:
            mult(a,b)
            loop==1
        elif opt==4:
            div(a,b)
            loop==1
    else:
        print("Quit!")
        loop-=1
