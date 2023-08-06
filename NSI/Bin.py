from math import pi

def ReelToBin():
    Entier_Bin = ""
    x = input("\nNombre Reel : ")
    if x == "pi" :
        x = pi
    elif x == "-pi":
        x = -pi
    else:
        x=float(x)
    if x < 0 :
        n = 2 ** 3
        while x < -n/2 :
            n = 2*n
        x = n + x
    Partie_Entière = int(x)
    if Partie_Entière != 0 :
        Entier_Bin = PartieEntiereToBin(Partie_Entière)
    else :
        Entier_Bin = "0"
    Partie_Décimal = x - int(x)
    Decimal_Bin = PartieDecimalToBin(Partie_Décimal)
    Nombre_Bin = Entier_Bin+","+Decimal_Bin
    print("\nNombre en binaire : "+Nombre_Bin)
    ReelToBin()

def PartieDecimalToBin(Partie_Décimal):
    Decimal_Bin = ""
    Partie_Entière = 0
    i = 0
    while 0 < Partie_Décimal and not Partie_Décimal == 1 and i < 25:
        i += 1
        Partie_Décimal = Partie_Décimal - Partie_Entière
        Partie_Décimal = Partie_Décimal*2
        Partie_Entière = int(Partie_Décimal)
        Decimal_Bin = Decimal_Bin+str(Partie_Entière)
    return Decimal_Bin

def PartieEntiereToBin(Partie_Entière):
    Entier_Bin = ""
    Quotient = Partie_Entière
    while Quotient > 0:
        Reste = Quotient % 2
        Quotient = Quotient // 2
        Entier_Bin = Entier_Bin+str(Reste)
    Inversed_Entier_Bin = ""
    i = len(Entier_Bin)
    while i > 0 :
     Inversed_Entier_Bin += list(Entier_Bin)[i-1]
     i -= 1
    return Inversed_Entier_Bin

ReelToBin()
