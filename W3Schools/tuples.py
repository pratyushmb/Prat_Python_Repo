myTuple = ("a", "b", "c")
print(myTuple)
print(myTuple[1])
print(myTuple[-1])
print(myTuple[1:2])

# change tuple value though its unchangable
myList = list(myTuple)
myList[1] = "change"
myTuple = tuple(myList)
print(myTuple)

# iterate thru tuple: need to verify
for x in myTuple:
    print(x)

if "change" in myTuple:
    print("yes this exists!")

# one item tuple, remember comma
oneItemTuple = ("hi",)
print(oneItemTuple)
print(type(oneItemTuple))

# tuple constructor

newTuple = tuple(("a", "b", "c"))
print(newTuple)
