x = lambda a: a + 10
print(x(6))

y = lambda a, b: a * b  # can take any number of arguments.
print(y(2, 3))

def my_function(a):
    return lambda b: a * b

mydoubler = my_function(2)
mytripler = my_function(3)

print(mydoubler(11))  # 22
print(mytripler(11))  # 33
