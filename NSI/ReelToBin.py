def PartieEntiereToBin(a):
    b= ""
    n = a
    while n != 0:
        b = str(n % 2)+b
        n = n // 2
    return(b)

def PartieDecimalToBin(a):
    b = ""
    n = a
    while n != 0:
        b = b+str(int(2*n))
        n = 2*n - int(2*n)
    return(b)

def ReelPositifToBin(x):
    n = x
    n_Entier = int(n)
    n_Decimal = n - int(n)

    Bin_Entier = PartieEntiereToBin(n_Entier)
    Bin_Decimal = PartieDecimalToBin(n_Decimal)

    Bin = Bin_Entier+","+Bin_Decimal
    return(Bin)

def ReelToBin(x):
    n = x
    p = 2**0
    if n < 0:
        while n < -p/2:
            p = 2*p
        n = n + p
    return(ReelPositifToBin(n))

while True :
    print(ReelToBin(float(input("ReelToBin : "))))
