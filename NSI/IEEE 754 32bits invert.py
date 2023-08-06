def CodeVirguleFlottante():
    NbDecimal = float(input("\nNombre decimal : "))
    if NbDecimal > 0:
        BinSigne = "0"
    elif NbDecimal < 0:
        BinSigne = "1"
        NbDecimal = -NbDecimal
    else:
        print("\nBinaire : 0")
        return

    NbBits=int(input("Nombre de bits 32/64 : "))
    if NbBits == 32:
        longExposant = 8
        longMantisse = 23
        facteurExposant = 127
    elif NbBits == 64:
        longExposant = 11
        longMantisse = 52
        facteurExposant = 1023


    PartieEntiere = int(NbDecimal)
    BinEntier = PartieEntiereToBin(PartieEntiere)

    PartieDecimale = NbDecimal - int(NbDecimal)
    BinDecimal = PartieDecimalToBin(PartieDecimale)

    NbBinaire = BinEntier+","+BinDecimal

    #Exposant
    Exposant = CalcExposant(NbBinaire)
    BinExposant = PartieEntiereToBin(Exposant+facteurExposant)
    #compléte les zéros manquants
    BinExposant = "0"*(longExposant-len(BinExposant))+BinExposant

    #print("Exposant = "+str(Exposant))
    #print("BinExposant : "+BinExposant)


    #Mantisse
    Mantisse = CalcMantisse(NbBinaire, longMantisse)

    #Affichage des 32 bits
    print("\nNombre Binaire IEEE754 : "+BinSigne, BinExposant, Mantisse)


    CodeVirguleFlottante()

def CalcExposant(NbBinaire):
    i = 0
    if NbBinaire[0] == ",":
        for bin in NbBinaire:
            if bin == "1":
                return i
            i = i-1
    else:
        for bin in NbBinaire:
            if bin == ",":
                i = i-1
                return i
            i = i+1

def CalcMantisse(NbBinaire, longMantisse):
    #conversion en liste
    NbBinaire = list(NbBinaire)
    #remplace les bits jusqu'au premier 1 sinificatif par ""
    i = 0
    for bin in NbBinaire:
        if bin == "1":
            NbBinaire[i] = ""
            break
        else:
            NbBinaire[i] = ""
        i = i+1
    Mantisse = NbBinaire

    #enlève la virgule
    i = 0
    for bin in Mantisse:
        if bin == ",":
            del Mantisse[i]
        i = i+1
    #enlève tous les ""
    while "" in NbBinaire:
        NbBinaire.remove("")

    #supprime les bits qui depasse de la norme
    while len(Mantisse) > longMantisse:
        del Mantisse[len(Mantisse)-1]

    #convertie la liste en string
    Mantisse =  "".join(Mantisse)


    #compléte les zeros manquants
    Mantisse = Mantisse+"0"*(longMantisse-len(Mantisse))

    return Mantisse







def PartieDecimalToBin(Partie_Décimal):
    #init var
    Decimal_Bin = ""
    Partie_Entière = 0
    #i est le nombre de chiffre après la virgule
    i = 0
    while 0 < Partie_Décimal and not Partie_Décimal == 1 and i < 25:
        i += 1
        Partie_Décimal = Partie_Décimal - Partie_Entière
        #print(Partie_Décimal)
        Partie_Décimal = Partie_Décimal*2
        #print(Partie_Décimal)
        Partie_Entière = int(Partie_Décimal)
        #print(Partie_Entière)
        #input()
        #print("\n")
        Decimal_Bin = Decimal_Bin+str(Partie_Entière)
    return Decimal_Bin

def PartieEntiereToBin(Partie_Entière):
    Entier_Bin = ""
    Quotient = Partie_Entière
    while Quotient > 0:
        Reste = Quotient % 2
        Quotient = Quotient // 2
        #print("\nQuotient : "+str(Quotient))
        #print("Reste : "+str(Reste))
        Entier_Bin = Entier_Bin+str(Reste)

    #inverser la chaîne de caractère
    Inversed_Entier_Bin = ""
    i = len(Entier_Bin)
    while i > 0 :
     Inversed_Entier_Bin += list(Entier_Bin)[i-1]
     i -= 1

    return Inversed_Entier_Bin

CodeVirguleFlottante()
