# Dictionaries - a collection of key - value paries
# like a phone book
point = {'x': 1, 'y': 2}
point2 = dict(x=1, y=2)
print(point['x'])
print(point2)

point['z'] = 20
print(point)


print('==================')
if "a" in point: print (point['a'])

# // how to know if the key exist and also retrive in 1 line ?
print(point.get('a','default')) # 'default' : default value
print(point.get('a',0),' <- 0 ,default, None -> ' ,point.get('a',None)) # 'default' : default value
print('we going to delete z key: ', point)
del point['z']
print(point)

print('==================')
print('Iteration over a dic')
for key in point :
    print (key,point[key])

print('== dic.items()  -> tupale')
for key in point.items() :
    print(key)

print('== dic.items()  -> distrauction')
for key, value in point.items() :
    print(key, value)