try:
    print(q)
except:
print("variable not defined")

###########

try:
    print("hello")
    print(r)
except:
    print("something is wrong")
else:
    print("nothing is wrong")
finally:
    print("code is done")
###################

# string formatting

price = 49
txt = "the price is {} dollars"
print(txt.format(price))

############
quantity = 5
itemno = 123
price = 49

myorder = "I want {} peices of item {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))
###########

# named index

myorder = "I need a {carname} , it is a {model}"
print(myorder.format(carname= "toyota", model="corolla"))
