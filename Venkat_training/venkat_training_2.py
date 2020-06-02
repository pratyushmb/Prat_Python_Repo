# import sys


def call_input():
    if int(input("Enter number of participants in PYTHON training ::")) > 2:
        print("INFO::Hurray..DI team has Good Team spirit in Learning PYTHON")
    else:
        print("INFO::Need Bigger team")

    team_list = input("Enter names of participants in training ::")
    print(team_list)
    if input("Enter Input String::") == "Python for DI Team":
        print("input matched")
    else:
        print("INFO::check input, expecting some string related to python training for DI team")


if __name__ == '__main__':

    call_input()

list1 = ['a', 'b', 'c']


for x in list1:
    print("the iteration is ", x)

# ENUM , RANGE, XRANGE

for x in range(5):
    print(x)

list2 = [1, 2, 3, 4]


for index, value in enumerate(list2):
    print(index, value)

# xrange: will keep only 1 element at a time in the memory but not present in Python 3

