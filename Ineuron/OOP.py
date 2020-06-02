class Person:
    pass

a = Person()
a.name = "pratyush"  # here name belongs to the Person class.
print(a.name)
print(type(a))

# #####################
class Person1:
    def __init__(self, name, surname):   # default method in python to initialize variables/arrtib.
        # self is pointer that referes to the object itself.
        self.name1 = name
        self.surname1 = surname
human = Person1("prat", "roy")
print(human)
print("my firstname is %s and lastname %s" % (human.name1, human.surname1))
# accessing object variables.


