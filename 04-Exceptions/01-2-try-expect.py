# ERROR example
# numbers = [1,2,3]
# // this will creat an exeption
# print(numbers[4])

try : 
    age = int(input("Your Age: "))
except ValueError as ex:
    print("You enter an invalid age.")
    # will print the error message
    print(ex)
    #  will prit: >class 'ValueError'>
    print (type(ex))
else :
    print(" no exceptions were thrown")

print("....")
print("....")
print("code continues")
