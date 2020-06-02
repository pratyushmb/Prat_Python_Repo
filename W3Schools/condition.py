a = 33
b = 33

if b > a:
    print("b is greater than a ")
elif a == b:
    print("both are equal")
# else
a = 30
b = 2
if b > a:
    print("b is greater than a")
elif a == b:
    print("both are same")
else:
    print("a is greater than b")

if a > b: print(" a is greater than b")

# WHILE LOOP

# Print i as long as i is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1

# With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# With else statement we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("now value of i " + str(i))

# FOR loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:

    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range
for x in range(2, 4):  # default increment is 1
    print(x)

for x in range(2, 8, 2):  # set increment as 2
    print(x)

# else keyword

for x in range(2, 5):
    print(x)
else:
    print("finished!")

# print prime numbers from 2 to 100

n = 2
while n <= 100:
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag is True:
        print(n)
    n = n + 1







