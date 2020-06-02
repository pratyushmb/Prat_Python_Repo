# __init__ function and object method


class Person:
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age

    def my_func(self):
        print("my name is " + self.fname)

p1 = Person("proy", 33)
print(p1.fname)
print(p1.age)
p1.my_func()

# inheritance

class Student(Person):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

x = Student("pratyush", "roy")
print(x.fname)
print(x.lname)
x.my_func()


# python iterator

mytuple = ("a", "b", "c")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystring = "abcde"
myit = iter(mystring)

print(next(myit))
print(next(myit))

# create an iterator

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# module

import mymodule
mymodule.greeting("pratyush")

# dates

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))  # RETURN NAME OF WEEKDAY


x = datetime.datetime(2020, 3, 27)
print(x)

