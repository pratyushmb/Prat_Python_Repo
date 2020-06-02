################################
name = 'tractor'
location, age = 'Brentwood', 40
# comment section
print(name)
print(location)
location = 'TN'
print(age)

print(location)

# del name  # deleting the variable physically from memory

print(name)
print(name)  # put cursor in prev line and ctrl D will copy to next line
#######################################

#  right click, local history , show history, will show all activities.
#  package management tool command: pip freeze > package_list.txt
#  use the file for QA , pip install -r package_list.txt

# Slicing and dicing on strings ################

name = "Tractor"
print("first character in our company is ", name[0])
print(name[1:4])  # Point to note the upper boundary is excluded.
print(name[1:])  # not specifying upper boundary.
print(name[:5])  # not specifying lower boundary.
print(name * 3)
print(name + " Supply Company")
print("I am %s company and I am %d years old" % ('Tractor', 80))  # formatting strings
print(name[-1])  # prints the last character of the string

# end slicing and dicing #############
name = 'tractor'
s = 't'
age = 80

x = name.encode(encoding='UTF-8', errors='strict')

print('the encoded version is: ', x)
print(s.join(name))
print(type(name))  # show data type
print(type(age))  # show data type
print(id(name))  # print location of data in memory
#####################

list1 = ["tractor", 40, 200.5, 'a', """ecomm
business"""]
print(list1[4])

################

dict1 = {'name': 'Tractor', 'age': 80, 900: 'tractor'}
pass  # pass statement is a null operation; nothing happens when it executes
dict1["di"] = "pradeep"  # adding a new key to the dictionary

print(dict1["di"])
print(dict1.keys())  # show all keys
print(dict1.values())  # show values
###############
