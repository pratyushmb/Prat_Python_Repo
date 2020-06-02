a = input("enter your name: ")
print("my name is {}".format(a))

'abc'.center(20, '#')  # will put data in center

x = 'abcde'
print(x.isalnum())  # alphanumeric or not.

# fibonachi series ######

n = int(input("enter the range: "))
def genfi():
    s = 1
    t = 1
    for i in range(n):
        s, t = t, s + t
        print(s)

genfi()
# end of fibo #########

# map() function: take 2 arguements: fucntion and sequence ############

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 10]

print(list(map(lambda p, q: p + q, a, b)))

def sum_num(x, y, z):
    return x + y + z

print(list(map(sum_num, a, b, c)))

# end of map(function, sequence i.e. list )

# reduce function ############
from functools import reduce

lst = [4, 3, 17, 1]
print(reduce(lambda r, s: r + s, lst))

max_val = lambda a, b: a if (a > b) else b
print(reduce(max_val, lst))

fct = [5, 4, 3, 2, 1]
factorial = reduce(lambda x, y: x * y, fct)
print(factorial)
# reduce function ############3

# filter function ############
def even_check(n):
    if n % 2 == 0:
        return True
lst = [1, 2, 3, 4, 5]
print(list(filter(even_check, lst)))

print(list(map(lambda a: a % 2 == 0, lst)))
# filter function ###############3


# list comprehensions 4th may vdo 1:36:49 frame######
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]

matrix = [lst1, lst2, lst3]  # list of multiple lists
print(matrix)

first_col = [row[0] for row in matrix]
print(first_col)


