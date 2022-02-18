def Polindrome(s):
    s = s.lower()
    s1 = s[::-1]
    s1 = s1.lower()
    if( s == s1):
        print("Polindrome")
    else:
        print("Not Polindrome")
m = Polindrome(input())
