class Parent:
    parentAttr = 100

    def __init__(self):
        print("in the parent constructor")

    def parentMethod(self):
        print("calling parent method")

    def setAttr(self, attrParent.parentAttr \
        = attr

    def
        getAttr(
            print("Parent attribute :“)
        print(
            Parent.parentAttr

    class Child(Parent):
        def

            init
        __(
            print("Calling child constructor“)

    def
        childMethod(
            print('Calling child method‘)
        c = Child()  # instance of child
        c.childMethod
        ()  # child calls its method
        c.parentMethod
        ()  # calls parent's method
        c.setAttr
        (200)  # again call parent's method
        c.getAttr \
        ()  # again call parent's method
