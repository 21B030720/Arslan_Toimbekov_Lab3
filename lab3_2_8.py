def James_Bond_Detecting(l):
    DetectorData = "".join(l)
    #print (DetectorData)
    if DetectorData.count("0 0 7"):
        print("This is James Bond!")
    else:
        print("Who is so handsome man")
k = James_Bond_Detecting(input())