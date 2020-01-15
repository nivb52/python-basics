numbers = list(range(4))

numbers.append('added')
print(numbers)

# Insert at spesific location : 
numbers.insert(2,1.5)
print(' Just added in the middle 1.5:  with *insert*')
print(numbers)
print('and here we can create app-bug : ')
numbers.insert(0,-2)
numbers.insert(0,-1)
print('because we need to think about the order')
print(numbers)

# Remove : 
numbers.pop()
print('Last item has been removed: with *pop*',numbers)
numbers.pop(1)
print('Second item has been removed: ',numbers)
num = 2
print(f'remove first appearance of {num} , with *remove*')
numbers.remove(num)
print(numbers)

 # Remove by del : 
print('remove mulitpale values : with *del*')
del numbers[2:]
print(numbers)

print('and now we will clear all: with *clear*')
numbers.clear()
print(numbers)
