# destructering

numbers = [1, 2, 3]
# LONG OPTION :
first = numbers[0]
second = numbers[1]

# OR LIKE THIS :
first, second, third = numbers
print(first, second, third)
print("But we must take all numbers from the list ")
print("the solution is to use for the rest with  - *otherVars")

numbers = list(range(20))
first, *rest, last = numbers
print(" like so: ", first, last)
print(" the rest: ", rest)