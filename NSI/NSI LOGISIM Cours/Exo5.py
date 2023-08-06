alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXY"
def code_cesar(sens, cle, texte):
    nouveautexte = ""
    for caractère in texte:
        i = 0
        if caractère in alphabet:
            while caractère != alphabet[i]:
                i=i+1
            if sens == "C":
                caractère = alphabet[i+cle]
            elif sens == "D":
                caractère = alphabet[i-cle]
        nouveautexte = nouveautexte + caractère
    return nouveautexte

print("Ave Caesar Morituri te Salutant ")
print(code_cesar("C", 2, "Ave Caesar Morituri te Salutant "))
print(code_cesar("D", 2, code_cesar("C", 2, "Ave Caesar Morituri te Salutant ")))
