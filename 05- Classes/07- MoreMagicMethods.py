# - Comparing Objects
# rszalski.github.io/megicmethods

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__ (self,other):
        return self.x == other.x and self.y == self.y

    def __gt__ (self, other):
        return self.x > other.x and self.y > other.y

point1 = Point(10,2)
point2 = Point(5,1)
bigPoint = Point(25,25)

# EQUAL
point3 = Point(0,2)
point4 = Point(0,2)

print('Are point 1 bigger than 2 ? ',point1 > (point2))
print('Are point 1 bigger than bigPoint ? ',point1 > (bigPoint))
print('Are point 3 and 4 Equal ? ',point4 == (point3))
print('And python give us : ===>  LESS THAN')
print('Are point 1 less than bigPoint ? ',point1 < (bigPoint))