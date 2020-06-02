# print data types

x = 5
y = "a"
z = 1j  # complex data type

print(type(x))
print(type(y))
print(type(z))
#####
p = 1
q = 2.3

r = int(q)
print(r)
#####

import random
# print(random.randrange(1, 5))  # print randomly 1 number
# generate random integer with minimum value 5 and max 11.
print(random.randint(5, 11))
print(random.randrange(5, 12, 1))
###
# type custing

x = int(2.4)
print(x)
y = int("223")
print(y)
# type casting

a = "Hello World!"
print(a[1])
print(a[2:5])
print(len(a))  # length of a string

x = " Before and After space "
print(x.strip())  # trim function
print(x.lower())  # lowercase
print(x.upper())  # uppercase
print(x.replace("s", "X"))  # replace a char
print(x.split(" "))  # split string based on separator and put it in a list
###
y = "hi friends hello"
a = "hi" in y
print(a)  # print boolean true
if "hih" in y:
    print("exactly")
else:
    print("not really")
###

age = 33
print(" my age is " + str(age))

txt = "My new age is {}"
print(txt.format(age))  # using format method to pass arguement

a = 1
b = 2
c = 3
txt = "I am number {} , then number {} and then number {}"
print(txt.format(a, b, c))
txt = "I am number {2} , then number {0} and then number {1}"
print(txt.format(a, b, c))
####

txt = "hi \" pratyush \" , how are you"
print(txt)

print("hello \"hi\" world \n my name \t it's tab and it's backslash \\")

name = "pratyush"
age = 32
sex = "M"
sal = 55.5

p = "my name is {} \n my age is {} \n sex is {} \n salary {}"
print(p.format(name, age, sex, sal))

# boolean
print(10 > 9)

class myclass():
    def _len_(self):
        return 0

myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x, int))

# lists

myList = ["a", "b", "c", "d", "e"]
print(myList)
print(myList[0])
print(myList[-1])
print(myList[2:4])  # range. The search will start at index 2 (included) and end at index 4 (not included).
print(myList[:3])  # By leaving out the start value, the range will start at the first item. i.e. a,b,c
print(myList[3:])  # By leaving out the end value, the range will go on to the end .

myList = ["a", "b", "c", "d", "e"]
print(myList[-4:-1])  # returns the items from index -4 (included) to index -1 (excluded)
# #Remember that the last item has the index -1

myList[2] = "change"  # update any value ith index
print(myList)

thisList = ["a", "b", "c"]  # loop thru list
for x in thisList:
    print(x)

if "z" in thisList:  # if an item exists
    print("yes it exists!")
else:
    print("no it doesnot!")
    print(len(thisList))

# To add an item to the end of the list, use the append() method

myList = ["a", "b", "c"]
myList.append("d")

print(myList)

# To add an item at the specified index, use the insert() method

myList = ["a", "b", "c"]
myList.insert(1, "d")
print(myList)

myList.remove("b")
print(myList)

# The pop() method removes the specified index
myList.pop(1)
print(myList)

del myList
myList.clear()
print(myList)

# copy a list
myList = ["a", "b", "c"]
cpyList = myList.copy()  # copy method
print(cpyList)

cpyList1 = list(cpyList)  # list method to copy
print(cpyList1)

# join 2 lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Use the extend() method to add list2 at the end of list1
list1.extend(list2)
print(list1)




