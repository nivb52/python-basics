# 22- Unpacking EXMAPELS
print('22- Unpacking --> REST IN JS')

print('         list(range(5)) : ')
values = list(range(5))
print(values)

# 2nd OPTION :
print('         [*range(5)] : ')
values = [*range(5)]
print(values)
# ALSO FOR STRING
print('# ALSO FOR STRING')
values = [*'Hello Uri']
print(values)

# CONCAT WITH *
first = [1]
second = [3,4]
values = [*first,*second]
print(values)


# ALSO FOR DICTONERY
point1 = {'x' : 11, 'y': 33} 
point2 = {'x' : 211, 'y': 433} 
print({**point1,**point2, 'z':0})
