from random import *
from math import e

def aireCourbeXcarre(N):
    n = 0
    borneX1 = 0
    borneX2 = 0.1
    for i in range(N):
        x = uniform(borneX1, borneX2)
        y = uniform(0, borneX2**2)
        if y <= x**2:
            n = n+1
    rate = n/N
    airetotale = abs(borneX2-borneX1)*borneX2**2
    aire = rate*airetotale
    print(aire)

#aireCourbeXcarre(10**6)
def aireCourbeEtoXpower(N):
    n = 0
    borneX1 = -100
    borneX2 = 1
    for i in range(N):
        x = uniform(borneX1, borneX2)
        y = uniform(0, e**borneX2)
        if y <= e**x:
            n = n+1
    rate = n/N
    airetotale = abs(borneX2-borneX1)*e**borneX2
    aire = rate*airetotale
    print(aire)


aireCourbeEtoXpower(10000000)
