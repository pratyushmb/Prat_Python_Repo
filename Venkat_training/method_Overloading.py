class Parent:
    def myMethod(self):
    print("Inside parent method")

class Child(Parent):
    def myMethod(self):
    print("Inside child method")

c = Child()
c.myMethod()
