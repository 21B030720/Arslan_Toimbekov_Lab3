import math
def filter_prime(l):
    for i in l:
        i = float(i)
        truth = True
        m = int(i**0.5)
        #print(m)
        for j in range(2, m+1):
            if( int(i) % j == 0):
                truth = False
                break
        if(truth):
            print(int(i), end = " ")
filter_prime(input().split())