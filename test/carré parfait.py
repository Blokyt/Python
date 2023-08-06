from math import *

def is_perfect(x):
    return sqrt(x)-int(sqrt(x)) == 0

def all_perfect_in_rangeOF(n):
    for x in range(2,n):
        if is_perfect(x):
            print(x, sqrt(x))
    all_perfect_in_rangeOF(int(input()))

all_perfect_in_rangeOF(int(input()))
