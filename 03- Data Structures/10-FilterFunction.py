items = [
    ("Aluminum", 10),
    ("Plastic", 1),
    ("Gold", 130),
    ("Silver", 23),
    ("Glass", 4),
]


# // Using the filter Method 

filter_object = filter(lambda item: item[1]>=10, items)
print('the filter object :',filter_object)
prices = list (filter_object)
print('and as list prices:')
print(prices)