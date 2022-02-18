def reverse(l):
    l.reverse()
    for i in l:
        print(i, end = " ")
reverse(input().split())