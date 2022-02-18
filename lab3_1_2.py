class Shape:
    area = 0
    def __init__(self, length):
        self.length = int(length)
    def area(self):
        print(self.area)


class Square(Shape):

    def area(self):
        area = self.length**2
        print(area)
m = Square(input())
m.area()