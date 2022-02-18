class Bank_Arslanya:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, money):
        self.balance += int(money)
        print("Your balance is " + str(self.balance))
    def withdraw(self, money):
        if(self.balance >= int(money)):
            self.balance -= int(money)
            print("Your balance is " + str(self.balance))
        elif(self.balance > 0):
            print(str(self.balance) + " was received")
            self.balance = 0
        else:
            print("You have no money")
m = Bank_Arslanya(input())
m.deposit(input())
m.withdraw(input())
m.withdraw(input())
