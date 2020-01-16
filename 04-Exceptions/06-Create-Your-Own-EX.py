def calculateAge(age):
    if age < 18:
        raise ValueError(" you are too small to drink")
    else:
        return True


try:
    if calculateAge(15):  # we gonna have an error
        print('we are doing something ...')
except ValueError as error:
    print(error)

finally:
    ("thank you for your support")
