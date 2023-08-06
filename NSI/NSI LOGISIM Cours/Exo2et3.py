def JeFaisQuoi(machaine) :
    i=0
    nombre=0
    while i<len(machaine):
        if machaine[i]=="e":
            nombre=nombre+1
        i=i+1
    return(nombre)

#machaine = "e"
#print(JeFaisQuoi(machaine)

def YaTilUnE(machaine) :

    if JeFaisQuoi(machaine) > 0 :
        return True
    else:
        return False
        
#machaine = "e"
#YaTilUnE(machaine)