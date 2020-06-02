
# task 1:2 ###########
i = 2000
a = ""
while i <= 3200:
    if i % 7 == 0 and i % 5 != 0:
        a += (str(i) + ",")
    i += 1
print(a)

# task 1:2 alternate ################
i = 2000
a = []
while i <= 3200:
    if i % 7 == 0 and i % 5 != 0:
        a.append(i)
    i += 1
print(a)

#  task 1:3  #############################
x = input("your first name: ")
y = input("your last name: ")

print(y + " " + x)

#    task 1:4    #############################
# V=4/3 * π * r 3
pi = 3.14
r = 12
V = 4/3 * 3.14 * (r ^ 3)
print("volume is: " + str(V))

#   task 2:1  #############################

y = input("enter comma separated numbers: ")

numbers = y.split(',')
print(numbers)

#  task 2:2    ##############################

n = 5
for i in range(n):
    # print(i)
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')

#     task 2:2   ##################################################

n = 5
for i in range(n):
    # print(i)
    for j in range(i):
        print("", end='* ')
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print("", end='* ')
    print('')

#   task 2:3    ######################################
i = 0
y = ""
x = input("enter the word: ")
z = len(x)
while i < z:
    y += x[z-1]
    z -= 1
print(y)

# task 2:4 ###########################################

print("""WE THE PEOPLE OF INDIA, \t \t \t \t \t
\t \t having solemnly resolved to constitute India into a SOVEREIGN, !
\t \t \t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
\t \t \t \tand to secure to all its citizens""")

# task 2:4 ###########################################



