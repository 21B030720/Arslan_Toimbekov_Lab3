class Primes:
    def __init__(self, max):
        self.max = max
        self.printer()
    def printer(self):
        l = []
        for i in range(2, self.max):
            l.append(i)
        l = list(filter(lambda p: all(map(lambda i: p % i != 0, range(2, p-1))), l))
        for i in l:
            print(i, end = " ")
        #print(list(filter(lambda p: all(map(lambda i: p & i, range(2, p - 1))), l)))
m = Primes(int(input()))