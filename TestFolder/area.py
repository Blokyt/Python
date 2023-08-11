from math import *

def area1(x, area=0):
    print(x, area)
    new_area = area+x**2-(x/2)**2*pi
    new_x = x/sqrt(2)
    if new_area == area:
        return
    area1(new_x, new_area)

area1(1)
