myDict = {
    "name": "prat",
    "age": 33,
    "place": "kol"
}

print(myDict)
x = myDict["age"]  # get the value of age key
print(x)

myDict["age"] = 34
print(myDict)

# loop thru a dictionary
for x in myDict:
    print(x)  # this will print key names only
    print(myDict[x])  # this will print all vallues

for y in myDict.values():
    print(y)  # this will print values as well

# Loop through both keys and values, by using the items() function
for x, y in myDict.items():
    print(x, y)

if "age" in myDict:
    print("yes, age is there")

myDict["hobby"] = "football"
print(myDict)

# remove item
myDict.pop("place")
print(myDict)

# Make a copy of a dictionary with the copy() method
newDict = myDict.copy()
print(newDict)

# Create a dictionary that contain three dictionaries , Nested dict

myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}

print(myfamily)

