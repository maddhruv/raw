#credit card verification
def sumTWOOO(z):
        ones= z%10
        twoes= z/10
        sumInside = ones + twoes
        return sumInside
number = "empty"
number = str(input("Enter the credit card number:"))
len = len(number)
if len != 16:
    print("Error! Enter 16 digit number!")
else:
    sum = 0
    stwo = 0
    for y in range (0, 16, 2):
        twoTimes =  2*int(number[y])
        if twoTimes>9:
            twoSum=0
            twoSum = sumTWOOO(twoTimes)
            stwo= stwo+twoSum
        else:
            stwo=stwo+twoTimes
    for x in range (1, 16, 2):
        sum = sum + int(number[x])
    total = sum + stwo

    if total%10 != 0:
        print("Error! The credit card number is invalid! Please enter correct number!")
    else:
        print("Successfull!")
