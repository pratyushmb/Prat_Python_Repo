def my_function(f_name):
    print("my first name " + f_name)

my_function("pratyush")

# for arbitraty arguments, use * and pass values as tuple.

def my_function(*name):
    print("all the names are: " + name[2])

my_function("a", "b", "c")

# keyword arguments

def my_function(c1, c2, c3):
    print("the value is : " + c3 + c1 + c2)

my_function(c1="v1", c2="v2", c3="v3")

# arbitrary keyword arguments

def my_function(**a):
    print("my last name is " + a["lname"])

my_function(fname="prat", lname="roy")

# arbitrary keyword arguments

# default parameter

def my_function(name="proy"):
    print("my name is " + name)

my_function("roy")
my_function("prat")
my_function()


# passing list as argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["a", "b", "c"]
my_function(fruits)

# return values

def my_function(x):
    return 5 * x

print(my_function(1))
print(my_function(2))

