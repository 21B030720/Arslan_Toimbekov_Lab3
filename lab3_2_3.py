def solve(numheads, numlegs):
    chicken = int(numheads)
    rabbit = 0
    while(chicken*2 + rabbit*4 < int(numlegs)):
        chicken -=1
        rabbit += 1
    print("Chickens: " + str(chicken))
    print("Rabbits: " + str(rabbit))
solve(input(), input())