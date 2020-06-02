# Task 1 : 1

def divide_five(a, b):
    c = a / b
    try: print("the division value: ", c)
    except ZeroDivisionError as e:
        print("INFO: error captured!")
        print(e)
    finally:
        print("finally the operation is done")

x = int(input("enter the dividend:"))
y = int(input("enter the divisor:"))
divide_five(x, y)

# TASK 1: 2 #######################

subjects = ["Americans ", "Indians"]
verbs = ["play", "watch"]
objects = ["Baseball", "Cricket"]

for x in subjects:
    for y in verbs:
        for z in objects:
            print(x + " " + y + " " + z)

# TASK 2: 1 ##########################

# column of the output matrix are power of the input vector
import numpy as np

x = np.array([1, 2, 3, 4, 5])
N = 4
print(np.vander(x, N))


