class Triangle():
    def first(self):
        base=5
        height=10
        ar=1/2*base*height
        print("Triangle area is ")
        print(ar)

class Rectangle(Triangle):
    def second(self):
        len=4
        bre=6
        area=len*bre
        print("Rectangle Area is ")
        print(area)
obj = Rectangle()
obj.first()
obj.second()