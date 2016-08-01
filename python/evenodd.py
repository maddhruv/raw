x = int(input('Enter the number:'))
if x%2==0:
	print('Even')
else:
	print('Odd')
	if x%3!=0:
		print('not divisible by 3')
