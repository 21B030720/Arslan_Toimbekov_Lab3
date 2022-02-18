class Point:
    pos1 = str(0)
    pos2 = str(0)
    def show(self):
        print(self.pos1 + " " + self.pos2)
    def move(self):
        self.pos1, self.pos2 = input().split()
    def dist(self):
        second_pos1, second_pos2 = map(int, input().split())
        pos1 = int(self.pos1)
        pos2 = int(self.pos2)
        print(   ( (pos1-second_pos1)**2 + (pos2-second_pos2)**2 )**(0.5)   )

m = Point()
m.move()
m.show()
m.dist()