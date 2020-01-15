point = ()
a = 1,2
b = (2, 3) + (5, 6)
c = (1, 2) * 3

print(point, type(point))
print(a , type(a))
print(b, type(b))
print(c, type(c))

print('--- more')
d = tuple([1,2])
print('*tuple( var )',d, type(d))

point = (1,2,3)
print('get only part from a tuple : [1:2]',point[1:2])

x, y ,*rest = b
print('destructering: ',x,y, '  from: ',b)

