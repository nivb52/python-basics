x = 10
y = 5
print('x:', x, ' y:', y)
# swapping vars with no extra var
x = x + y
y = x - y
x = x - y
print('x:', x, ' y:', y)

# more advance speial for python :
x = 100
y = 50
print('using tupale + destructering: ')
print('x:', x, ' y:', y)
print('x, y = y, x')
# x , y = y, x   --> tupple'
#  like x,y = 10 ,5
# and we unpacking/destructering it
x, y = y, x
print('x:', x, ' y:', y)
