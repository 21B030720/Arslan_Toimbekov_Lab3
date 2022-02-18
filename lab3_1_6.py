class Data:
    def __init__(self, l):
        self.l = l
    def filter(self, a):
        l = filter(lambda x: all(map(lambda x: x % i == 0)))