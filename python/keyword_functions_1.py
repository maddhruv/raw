def dhruv(name, *arg, **key):
    print("-- My name is "+ name)
    print("-"*20)
    for ar in arg:
        print(ar)
    print("*"*20)
    k=sorted(key.keys())
    for x in k:
        print(x+" : "+key[x])

dhruv("dhruv", "my name is dj", "my age is 18", work="student", status="single")
