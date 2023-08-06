from math import *

def lambert_funct(w_log, x=0):
    old_x = None
    new_x = x
    while new_x != old_x:
        old_x = new_x
        new_x = old_x-(old_x*e**old_x-w_log)/(old_x*e**old_x+e**old_x)
    print(new_x)
    return new_x



#lambert_funct(1, 2)

def ln_func(log, x=0):
    old_x = None
    new_x = x
    while new_x != old_x:
        old_x = new_x
        new_x = old_x-(e**old_x-log)/(e**old_x)
    print(new_x)
    return new_x

ln100 = ln_func(100)
wof5ln100 = lambert_funct(5*ln100)


print(e**(wof5ln100/5))
