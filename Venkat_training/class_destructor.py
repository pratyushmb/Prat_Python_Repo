class TscEmp:
    """This is a template creating tsc emp"""
    empCount = 0

# Constructor assigning values to instance variables.
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
        TscEmp.empCount += 1

    def __del__(self):
        className = self.__class__.__name__
        print(className)
        print("is destroyed")
        TscEmp.empCount -= 1


# Creating objects for TscEmp class
emp1 = TscEmp("John", 100, "Manager")
emp2 = TscEmp("prat", 200, "developer")

# Accessing the methods of the class via object
print("Employee count before deleting the object:")


print(TscEmp.empCount)

del emp1

print("Employee count AFTER deleting OBJECT is ")
print(TscEmp.empCount)
