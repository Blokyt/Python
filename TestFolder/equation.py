from math import *

def solve():
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("c : "))
    delta = (b*b)-(4*a*c)
    print("delta : "+str(delta))
    if delta > 0 :
        x1 = (-b-sqrt(delta))/(2*a)
        x2 = (-b+sqrt(delta))/(2*a)
        print("x1 : "+str(x1))
        print("x2 : "+str(x2))
    elif delta == 0:
        x = (-b)/(2*a)
        print("x : "+str(x))
    else:
        x1 = (-b-1j*sqrt(-delta))/(2*a)
        x2 = (-b+1j*sqrt(-delta))/(2*a)
        print("x1 : "+str(x1))
        print("x2 : "+str(x2))


solve()
