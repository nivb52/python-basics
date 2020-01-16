class MyPoint:
    # // instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # ==============
    # Class Method:
    @classmethod
    def zero(cls):
        return cls(0, 0)   # cls => short for class
    # ^^^^^^^^^^^^^^
    
    # // Instance Method
    def draw(self):
        print(f"Point ( {self.x} , {self.y} )" )


point = MyPoint.zero()
point.draw()

def someMtd():
    print('try changing class method')

# .. YOU CANT CHANGE CLASS METHOD REGULLARY
point.zero =  someMtd
print(point.zero())
print("And yet it's a class method only (saying None [=null])")
point.draw()