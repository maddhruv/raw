D = {1:"one", "do":"two", "pi":3.14}
D1=D
print(D)
D1[1]="uno"
print(D1[1])
for k in D1.keys():
	print(k,"=",D1[k])
del D1[1]
print(D1)