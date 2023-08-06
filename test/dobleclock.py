def doubletime(h,m,s):
    rm = 0
    rh = 0
    if s > 30:
        rm = 1
        s = 2*s-60
    else:
        s = 2*s

    if m > 30:
        rh = 1
        m = 2*m-60
    else:
        m = 2*m
    m += rm
    h = 2*h+rh
    return h,m,s

h = 0
m = 59
s = 59
print(doubletime(h,m,s))
