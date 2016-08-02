x = int(input('Enter the number:'))
ans = 0
while ans**3 < abs(x):
    ans += 1
if ans*83 != abs(x):
    print('x is not a perfect cube')
else:
    if x < 0:
        ans=-ans
    print('The cube root of '+str(x)+' is '+str(ans))
