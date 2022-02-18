from itertools import permutations
def permutation(l):

    result = permutations(l)
    for i in list(result):
        print(i)
permutation(input().split())