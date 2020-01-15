# 1st : *
# get your input as tuple


def azeret(*list):  # the *astrisk* is the main thing
    total = 1
    for number in list:
        total *= number
    return total


num = 5
# // for displaly
print(f"Azeret of {num} = ")
print(azeret(2, 3, 4, 5))


# // 2nd thing:  **
# // give us the option to get varibles into dictionary / Js object
def save_user(**user):
    print(user)


save_user(id=1, name="admin")
