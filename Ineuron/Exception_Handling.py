# continuously checking for user input
def askint():
    while True:
        try:
            v = int(input("enter a value: "))
        except Exception as e:
            print(e)
            break
        else:
            print("I am an integer")
            break
        finally:
            print("Finally I am executed")
            print(v)

askint()

# ###################
try:
    f = open('a.txt')
    f.write("my name is prat")
except FileExistsError as e:
    print(e)
except ValueError:
    print("it is value error")
except FileNotFoundError:
    print("this is file not found error")
except IOError:
    print("this is IO error")
except Exception as ex:
    print("this is some other exception")


try:
    f = open('a.txt')
    f.write("my name is prat")
except (FileExistsError, ValueError, IOError, OSError):
    print(" there is an error in the code")

# custom exception ##################

try:
    v = int(input("try to input an integer"))
    if v < 2:
        raise ValueError("this is not proper value")
except ValueError as e:
    print(e)

# custom exception ##################

try:
    v = int(input("try to input an integer"))
    f = v / 2
    if v == 2:
        raise ValueError("this is not proper value")
except ValueError as e:
    print(e)

# custom exception ##################

