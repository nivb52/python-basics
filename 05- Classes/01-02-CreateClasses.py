class MyPoint :
    def draw(self):
        print("draw")
    


point = MyPoint()
print(type(point))
print(isinstance(point, MyPoint))