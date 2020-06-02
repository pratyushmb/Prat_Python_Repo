findsum = lambda arg1, arg2: arg1 + arg2;

print(findsum(10, 20))


def myfunc(n):
    return lambda a: a*n


mydoubler = myfunc(2)
print(mydoubler(11))

print(type(mydoubler))
