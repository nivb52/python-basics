# // METHOD 1 : 

try:
    file = open("04-cleaning-up.py")
    print("if we have an error now the file will remain open")
    print("if it remain open no one will be able to access it")
    print("so we need to close it")
    age = int(input('enter your name: '))
    # we will not reach it and the file will be block in case of error 
    # file.close()
except (ValueError):
    print('we have a code mistake, please enter number next time')
    # close it here is not best practice
    # because we need to close it any wayand we dont want to
    # write same line twice
    # file.close()
else :
    print('every thing went smooth')

finally: 
    file.close()


print(' but there is better way - we can use WITH steatment to close the file automatic ')
