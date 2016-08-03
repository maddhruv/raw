X=int(input("Enter the amount to withdraw: "))
Y=float(input("Enter the initial amount: "))
if Y>=X+0.50:
    if X%5==0:
        print("Amount left in the account:"+str(Y-X-0.50))
    else:
        print("It should be multiple of 5")
else:
    print("Insufficient Balance!")
