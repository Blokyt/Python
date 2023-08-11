def sommeImp(n):
    s = 0
    for i in range(1,2*n,2):
        print(i)
        s = s+i
    return s

print(sommeImp(10))
