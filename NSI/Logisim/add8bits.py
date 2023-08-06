def SommeBinaire(a,b):
    a = list(a)
    b = list(b)
    c = ""
    r = 0
    for bits in range(1, len(a)+1):
        if (int(a[len(a)-bits])^int(b[len(a)-bits]))^r:
            s = 1
            r = 0
            if int(a[len(a)-bits]) and int(b[len(a)-bits]):
                r = 1
        elif int(a[len(a)-bits]) and int(b[len(a)-bits]) or c and int(a[len(a)-bits]) or c and int(b[len(a)-bits]) :
            r = 1
            s = 0
        else:
            s = 0
            r = 0
        c = str(s)+c
    print(c)


a = "00001101"
b = "11110011"

SommeBinaire(a, b)

#for bita1 in [0,1]:
    #for bita2 in [0,1]:
        #for bita3 in [0,1]:
            #for bita4 in [0,1]:
                #a = str(bita1)+str(bita2)+str(bita3)+str(bita4)
                #for bitb1 in [0,1]:
                    #for bitb2 in [0,1]:
                        #for bitb3 in [0,1]:
                            #for bitb4 in [0,1]:
                                #b = str(bitb1)+str(bitb2)+str(bitb3)+str(bitb4)
                                #print(a)
                                #print(b)
                                #SommeBinaire(a, b)
                                #print("\n")
