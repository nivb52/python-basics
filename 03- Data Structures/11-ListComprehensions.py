# 11-List Comprehensions
# not exsit in other lang
items = [
    ("Aluminum", 10),
    ("Plastic", 1),
    ("Gold", 130),
    ("Silver", 23),
    ("Glass", 4),
]


print('Comprehensions - better in preformance and loved in the python community')
# prices = map(lambda item: item[1], items)
# AND IN Comprehensions :
prices = [ item[1] for item in items ]
print(items)

# filter_object = filter(lambda item: item[1]>=10, items)
print('filtered = [expression for item in items]')
print( [item[1] > 10 for item in items ])
# 2nd phase : 
filtered = [ item for item in items if item[1] >= 10 ]
print(filtered)
