class Shape:
    area = 0
    def __init__(self, length):
        self.length = int(length)
        self.area()



class Rectangle(Shape):
    def area(self):
        width = int(input())
        print(self.length * width)

m = Rectangle(input())