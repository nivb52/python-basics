items = [
    ("Aluminum", 10),
    ("Plastic", 1),
    ("Gold", 130),
    ("Silver", 23),
    ("Glass", 4),
]

# // transform it to list of prices
prices = []

# // option 1
for item in items : 
    prices.append(item[1])
print('option 1: ',prices)


# // option 2
prices = map(lambda item: item[1], items)
print('option 2: a. create map object  ',prices)
prices = list(prices)
print('option 2: b. convert to list ',prices)
