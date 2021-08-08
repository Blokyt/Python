grille = []
ligne = int(input('lignes : '))
colonne = int(input("collonnes : "))

def initialisation_grille (ligne,colonne,grille):
    for x in range(ligne) :
        grille.append([])
        for y in range(colonne) :
            grille[x].append("0")

def reinitialisation_grille(grille):
    for x in grille :
        for y in range(colonne) :
            x[y] = "0"
            affichage_grille (grille, ligne)

def affichage_grille (grille, ligne) :
    print("\n")
    for x in range(1,ligne+1):
        print(grille[ligne-x])

def placer_jeton (jeton_joueur, grille, ligne, colonne) :
    n = 0
    for x in grille[ligne-1] :
        if x != "0" :
            n = n + 1
    if n == colonne :
        print("\nEgalite")
        reinitialisation_grille(grille)


    colonne_choisie = int(input("\nChoisie la colonne :"))

    if grille[ligne-1][colonne_choisie-1] != "0" :
        print("\ncolonne deja remplie ! ")
        placer_jeton (jeton_joueur, grille, ligne, colonne)
    else :
        for x in grille :
            if x[colonne_choisie-1] == "0":
                x[colonne_choisie-1] = jeton_joueur
                affichage_grille(grille, ligne)
                return

def start(grille, ligne, colonne):
    Victoire = False
    initialisation_grille(ligne,colonne,grille)
    affichage_grille(grille, ligne)
    while Victoire == False :
        placer_jeton("X", grille,ligne, colonne)
        if Victoire == False :
            placer_jeton("O", grille,ligne, colonne)

start(grille, ligne, colonne)
