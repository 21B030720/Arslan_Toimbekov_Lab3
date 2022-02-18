def  Trulian(l):
    pos = 0
    while(pos < len(l)-1):
        if l[pos] == "3":
            if l[pos+1] != "3":
                if pos > 0 and l[pos-1] != "3":
                    return "False"
        pos += 2
    if l[len(l)-1] == "3" and l[len(l)-2] != "3":
        return "False"
    return "True"


k = Trulian(input().split())
print(k)