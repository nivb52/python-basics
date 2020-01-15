def increment(number, by):
    return number + by


print(increment(2, 3))

# return Tuple


def increment2(number, by):
    return (number, number + by)


# defualt value to by : 1
# define number and by to int,
# define return to int
def increment3(number: int, by: int = 1) -> int:
    return number + by


increment3(2)


# // define what we send to the function, not by function order
def increment4(number: int, by: int ) -> int:
    return number - by

print(increment4(by = 2, number=10))
