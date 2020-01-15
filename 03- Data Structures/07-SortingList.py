numbers = [3,4,5,21,9,7,11,1,9,0,2,8]
numbers.sort()
print("we use *sort* and get:",numbers)

numbers.sort(reverse=True)
print("reverse=True:",numbers)

print('without modify the original list :')
print('*sorted(list)*',sorted(numbers))

# complex items: 
items = [
    ("Aluminum", 10),
    ("Plastic", 1),
    ("Gold", 130),
    ("Silver", 23),
    ("Glass", 4),
]
def someSortFunc(item) :
    return item[1]

print('complex items : use *list.sort(key = func)*')
items.sort(key=someSortFunc)
print(items)