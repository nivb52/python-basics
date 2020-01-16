#lets calculate the time this code takes
from timeit import timeit

code1 = """
def calculateAge(age):
    if age < 18:
        raise ValueError(" you are too small to drink")
    else:
        return True


try:
    if calculateAge(15):  # we gonna have an error
        print('we are doing something ...')
except ValueError as error:
    pass


"""
print('with raising ex = ', timeit(code1,number=123456)*100)


# ==================================
code2 = """
def calculateAge(age):
    if age < 18:
        return false 
    else:
        return True


    if calculateAge(15):  # we have IF BLOCK 
        print('we are doing something ...')

"""
# ===================================
print('CODE 2  = ', timeit(code2,number=123456)*100)
print("=== >")
print("code 2 is almost 4 times faster, (and not because of the line number)")