if 5 > 3:
    print("yes! 5 > 3")

x_y = "hello"  # variable can start with _ , cannot start with number, no other
# special character allowed.
print(x_y)

x, y, z = "a", "b", "c"
# x = y = z = "same"
print(x)
print(y)
print(z)

x = 5
y = "abc"
print(str(x) + y) # 5abc

# this is a comment

"""
this
is multi line
comment
"""

"""hi
this
is
"""

b = "x"
print("I am printing " + b)

a = 5
# this is error print("this is " + a)
print("I am printing " + str(a))

x = "pratyush "
y = "roy"
print(x + y)

# global variable
y = "hi there! "

def mychat():
    print("oh hello.." + y)

mychat()

# another example
x = "hi"

def mychat():
    x = "hello"
    print("within function " + x)

mychat()

print(x)

# global keyword
x = "hi"

def mychat():
    global x
    x = "hello"
    print("within function " + x)

mychat()

print("outside function " + x)


##############################
