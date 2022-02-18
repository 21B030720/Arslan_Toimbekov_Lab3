import math
def SphereVolume(r):
    r = float(r)
    print(4/3*(r**3)*math.radians(180))

m = SphereVolume(input())