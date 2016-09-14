def fun(a, l=[]):
    l.append(a)
    return l

fun(1)
fun(2)
print(fun('a'))
