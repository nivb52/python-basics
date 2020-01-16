class MyPoint :
    # // class attributes
    # shared in all class instances 
    default_color = 'red'

    # // instance attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"draw ({self.x}, {self.y})")



point1 = MyPoint(1,2)
point2 = MyPoint(3,4)
print('default_color: ',point1.default_color)
print('=============')
print('This Line: MyPoint.default_color = yellow ')
print('will change all class instances values')
MyPoint.default_color = 'yellow'
print(point1.default_color)
print(point2.default_color)