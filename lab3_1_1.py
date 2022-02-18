class task1:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = str(input())
        self.printString()
    def printString(self):
        print(self.string.upper())
m = task1()
m.getString()