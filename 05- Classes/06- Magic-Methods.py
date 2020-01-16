# rszalski.github.io/megicmethods

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point ( {self.x} , {self.y} )" )


point = MyPoint(1,2)

print(point)
# // <__main__.MyPoint object at 0x00C191D8>
# __str__ ^ give us the above which is magic methods
print(" __str__  gave us the ^ above which is magic methods")


# ===============


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # // magic method
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def draw(self):
        print(f"Point ( {self.x} , {self.y} )" )


point = Point(1,2)
print("===========CHANGING MAGIC METHODS======================")

print(point)
print(str(point))
# __str__ ^ give us the above which is magic methods
print(" ^ CHANGED __str__ ^ ")

#  ================ CANT CHANGE LIKE THIS : =======================
point2 = Point(0,0)
print(" # YOU CAN'T CHANGE IT BY ClassName.__str__  = some code ... ")
# YOU CANT CHANGE IT LIKE THIS
def someStr():
    print('haha')

point.__str__ = someStr

print(point)
print(point2)
