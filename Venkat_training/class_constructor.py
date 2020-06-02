class TscEmp:
    """This is a template creating tsc emp"""
    empCount = 0

# Constructor assigning values to instance variables.
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
        TscEmp.empCount += 1

    def displayCount(self):
        print("total emp till now %d", TscEmp.empCount)

    def displayEmployee(self):
        print("Employee name:", self.name)
        print("Employee role:", self.role)


# Creating objects for TscEmp class
emp1 = TscEmp("John", 100, "Manager")
emp2 = TscEmp("prat", 200, "developer")

# Accessing the methods of the class via object
emp1.displayEmployee()
emp2.displayEmployee()

print(TscEmp.__doc__)
print(TscEmp.__dict__)
