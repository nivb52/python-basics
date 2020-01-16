class MyPoint :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"draw ({self.x}, {self.y})")


point = MyPoint(1,2)
point.draw()