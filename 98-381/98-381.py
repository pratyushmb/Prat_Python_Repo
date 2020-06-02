x = (3*(1 + 2)**2 - (2**2)*3)
# 3*9 - 4*3
# 27 - 12 = 15
print(x)
###############

a = eval(input("enter the number: "))
a = 2
b = (-a)**2
print(b)

################

print("what is your name")
name = input()
print(name)
################
r = 5
if r == 5:
    print("hi")
else:
    print("hello")
##############

import os
def read_file(file):
    line = none
    if os.path.isfile(file):
        data = open(file, "r")
    while line != '':
    line = data.readline()
        print(line)
###############

import math
c = 2.65
# print(math.fmod(c)) # error
# print(math.frexp(c)) # (0.6625, 2)
# print(math.floor(c)) # absolute value 2
print(math.fabs(c)) # 2.65
print(math.ceil(c)) # 3

#########################
 import random

 y = random.randint(5,11)
 print(y)
 z = random.randrange(5,12,1)
 print(z)
 ###########

numlist = [1,2,3,4,5]
alphalist = ["a","b","c","d","e"]
x = [1,2,3,4,5]
print(numlist is alphalist)
print(numlist is x)
print(numlist == alphalist)
numlist = alphalist
print(numlist is alphalist)
print(numlist == alphalist)

###################################

p = 2
while p <= 100:
    is_prime = True
    for i in range(2, p):
        if p % i == 0:
            is_prime = False
            break
    if is_prime is True:
        print(p)
    p = p + 1

####################

a = 3
b ='ab'

print(a*b)
print(b*a)

print(not 10)

a = 45
b = 45
print(a is not b)

x1 = "20"
y1 = 3
a = x1 * y1
print(type(a))