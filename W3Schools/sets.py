mySet = {"a", "b", "c", "d"}
print(mySet)  # Sets are unordered, so not sure in which order the items will appear.

# You cannot access items in a set by referring to an index
# but can loop through

for x in mySet:
    print(x)

# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.

mySet.add("new")
print(mySet)
mySet.update(["new1", "new2"])
print(mySet)

mySet.remove("new2")
print(mySet)

# discard() function can be used to , if the item doesnot exist
# remove() will throw error whereas discard() will not.

# Remove the last item by using the pop() method which is random

x = mySet.pop()
print(x)  # will show the item that got deleted
print(mySet) # will show the rest of the items in set

# The union() method returns a new set with all items from both sets

newSet = {"n1", "n2"}
unionSet = newSet.union(mySet)
print(unionSet)

# The update() method inserts the items in set2 into set1:

set1 = {1, 2, 3}
set2 = {10, 20, 30}
set1.update(set2)
print(set1)
# Both union() and update() will exclude any duplicate items.

# set constructor
newSet = set((1, 2, 3))
print(newSet)

