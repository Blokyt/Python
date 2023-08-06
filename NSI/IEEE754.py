
def DecodeVirguleFlottante():
    NbBinaire=input("\nNombre binaire IEEE754 : ")
    NbBits=int(input("Nombre de bits 32/64 : "))
    NbBinaire = NbBinaire.replace(" ", "")
    BinSigne, BinExposant, BinMantisse = "", "", ""
    Signe, Exposant = int(0), int(0)
    Mantisse, nombre = float(0), float(0)

    if NbBits == 32:
        longExposant = 8
        longMantisse = 23
        facteurExposant = 127
    elif NbBits == 64:
        longExposant = 11
        longMantisse = 52
        facteurExposant = 1023
    #print(longEpoxant, longMantisse, facteurExposant)

    if len(NbBinaire) != NbBits:
        print("\nLa chaîne de caractère "+NbBinaire+" ne représente pas un réel codé en "+str(NbBits)+" bits")
    elif NbBinaire == NbBits*"0":
        print("\nNombre : 0")
        return
    else:
        BinSigne = NbBinaire[0]
        BinExposant = NbBinaire[1:longExposant+1]
        BinMantisse = NbBinaire[1+longExposant:NbBits]
        print("\n"+BinSigne, BinExposant, BinMantisse)
        if BinSigne == "1":
            Signe = -1
        elif BinSigne == "0":
            Signe = 1

        print("\nSigne : "+str(Signe))
        Exposant = ValeurDecimal(BinExposant, longExposant)-facteurExposant
        print("\nExposant : "+str(Exposant))
        Mantisse = 1+ValeurFractionnaire(BinMantisse)
        print("\nMantisse : "+str(Mantisse))
        Nombre = Signe * 2 ** Exposant * Mantisse
        print("\nNombre : "+str(Nombre))
        DecodeVirguleFlottante()

def ValeurDecimal(Bin, bits):
    decimal = int(0)
    e = 2 ** (bits-1)
    for bit in Bin:
        #print("\nbit = "+bit)
        #print("e = "+str(e))
        decimal = decimal + int(bit)*e
        e = e/2
    return decimal

def ValeurFractionnaire(Bin):
    decimal = int(0)
    e = 2 ** -1
    for bit in Bin:
        #print("\nbit = "+bit)
        #print("e = "+str(e))
        decimal = decimal + int(bit)*e
        e = e/2
    return decimal

DecodeVirguleFlottante()
