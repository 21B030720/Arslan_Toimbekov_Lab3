def unique(l1):
    l2 = []
    l22 = []
    for i in l1:
        if i.lower() not in l22:
            l2.append(i)
            l22.append(i.lower())
    for i in l2:
        print(i, end = " ")

m = unique(input())