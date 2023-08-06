def SommeBinaire(a, b):
    #defini c comme la somme bits à bits de a + b
    c = ""
    #defini le reste
    r = 0
    #nombre de bits
    nbits = len(a)

    #lecture bits à bits des deux entrées
    for bits in range(1,nbits+1):
        #conversion et substitution des chaîne de caractère en liste pour acceder isoler chaque bits
        bit_a = list(a)[nbits-bits]
        bit_b = list(b)[nbits-bits]

        #première somme du demi-additionneur
        s1 = int(bit_a)^int(bit_b)
        #somme de a + b
        s = s1^r

        #debug print("s"+str(s))

        #premier reste du demi additionneur
        r1 = int(bit_a) and int(bit_b)
        #second reste de l'additionneur
        r2 = s1 and r
        #reste
        r = r1 or r2

        #debug print("r"+str(r))
        c = str(s)+c
        #debug print("c"+str(c))

    #prise en compte du bit sortant
    if r == 1:
        c = "1"+c

    #retourne la somme bits à bits de a + b
    return c

#entrée
a = input("Nombre binaire : ")
b = input("Nombre binaire : ")

#equilibrage du nombre de bits
while len(a) != len(b):
    if len(a) < len(b):
        a += "0"
    else:
        b += "0"

#affiche ce que nous retourne la fonction SommeBinaire(a, b)
print(SommeBinaire(a, b))
