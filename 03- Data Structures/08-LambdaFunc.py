# complex items sort: 
# using lambda function
items = [
    ("Aluminum", 10),
    ("Plastic", 1),
    ("Gold", 130),
    ("Silver", 23),
    ("Glass", 4),
]

# def someSortFunc(item) :
#     return item[1]

print("""sort complex items : 
use * list.sort(key = func)*
""")
items.sort(key=lambda item: item[1])
print(items)