import random
def GuessTheNumber():
    print("Hello! What is your name?")
    name = input()
    print("Well, {0}, I am thinking of a number between 1 and 20.".format(name))
    sum = 0
    given = random.randrange(1, 20)
    print(given)
    m = int(input())
    while(m != given):
        sum += 1
        if m < given:
            print("Your guess is too low.")
        else:
            print("Your guess is too up.")
        print("Take a guess.")
        m = int(input())
    print("Good job {0}! You guessed in {1} guesses".format(name, str(sum)))

m = GuessTheNumber()