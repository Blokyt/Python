def clock(A,B,C):
    tickdeg360 = 1/(1/12*10**-10)*360
    for deg in range(360):
        newA = A%tickdeg360-deg*1/(1/12*10**-10)
        newB = B%tickdeg360-deg*1/(1/12*10**-10)
        newC = C%tickdeg360-deg*1/(1/12*10**-10)
        for i in [newA,newB,newC]:
            for j in [newA,newB,newC]:
                for k in [newA,newB,newC]:
                    if i != j and j!= k and k != i or (A == B and B == C):
                        h = (i*10**-9)/3600
                        m = (j/12*10**-9)/60
                        s = k/720*10**-9
                        if s < 1:
                            nano = round(s*10**9)
                        else:
                            nano = 0
                        hpile = int(h)
                        mpile = int(m)
                        spile = int(s)
                        for l in range(-5,-2):
                            if hpile + m/60 - 10**l <= h <= hpile + m/60 + 10**l and mpile + s/60 - 10**l <= m <= mpile + s/60 + 10**l:
                                return hpile,mpile,spile,nano,deg
ninput = 3
input1a, input1b, input1c = 0, 11, 719
input2a, input2b, input2c = 0, 21600000000000, 23400000000000
input3a, input3b, input3c = 1476000000000, 2160000000000, 3723000000000

A = [input1a, input2a, input3a]
B = [input1b, input2b, input3b]
C = [input1c, input2c, input3c]
for i in range(ninput):
    print(clock(A[i],B[i],C[i]))
