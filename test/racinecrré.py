from math import *
def Heron(a,x=1, y=None, affiche=True):
    while x != y:
        if affiche : print(x)
        y = x
        x = 1/2*(x+a/x)

n = 100
p = 1
for i in range(1, n*p+1):
    i = i/p
    print(i)
    Heron(i)
    print("\n")
