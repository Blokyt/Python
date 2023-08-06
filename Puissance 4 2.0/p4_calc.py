from random import *

grille = []
ligne = 6
colonne = 7

def initialisation_grille (ligne,colonne,grille):
    for x in range(ligne) :
        grille.append([])
        for y in range(colonne) :
            grille[x].append(" ")

def reinitialisation_grille(grille):
    for x in grille :
        for y in range(colonne) :
            x[y] = " "

def affichage_grille (grille, ligne) :
    print("\n")
    for x in range(ligne):
        tableau = "["+"|".join(grille[ligne-(x+1)])+"]"
        print(tableau)

def placer_jeton (jeton_joueur, grille, ligne, colonne) :
    #affichage de la grille
    affichage_grille(grille, ligne)
    #Selection de la colonne du jeton
    colonne_choisie = input("\nChoisis la colonne : ")
    #Verification de l'entrée
    try:
        colonne_choisie = int(colonne_choisie)

    except ValueError:
        return placer_jeton (jeton_joueur, grille, ligne, colonne)
    if (0 < colonne_choisie <= colonne ) :
        pass
    else:
        return placer_jeton (jeton_joueur, grille, ligne, colonne)
    #Regarder si la colonne choisie est pleine
        #Si oui relance la fonction
    if grille[ligne-1][colonne_choisie-1] != " " :
        print("\nColonne deja remplie ! ")
        placer_jeton (jeton_joueur, grille, ligne, colonne)
        #Sinon placer le jeton
    else :
        for x in grille :
            if x[colonne_choisie-1] == " ":
                x[colonne_choisie-1] = jeton_joueur
                if check_board(grille, ligne, colonne,jeton_joueur) :
                    return True
                else :
                    return False


def check_board(grille, ligne, colonne,jeton_joueur) :

    #check draw
    filled_column = 0
    for symbole in grille[ligne-1] :
        if symbole != " " :
            filled_column += 1
    if filled_column == colonne :
        draw(grille)
        return True
    #check win

    for element in range(colonne-3):
        # print("\n")
        #check horizontal
        for hauteur in range(ligne):
            check_lign = [grille[hauteur][element+i] for i in range(0,4)]
            # print("checklign"+str(check_lign))
            if check_lign == 4*["X"] or check_lign == 4*["O"]:
                win(grille, ligne, jeton_joueur)
                return True

        #check diagonal gauche-droite
        for hauteur in range(ligne-3):
            check_lign = [grille[hauteur+i][element+i]for i in range(0,4)]
            # print("checklign"+str(check_lign))
            if check_lign == 4*["X"] or check_lign == 4*["O"]:
                win(grille, ligne, jeton_joueur)
                return True

        #check diagonal droite-gauche
        for hauteur in range(3,ligne):
            check_lign = [grille[hauteur-i][element+i]for i in range(0,4)]
            # print("checklign"+str(check_lign))
            if check_lign == 4*["X"] or check_lign == 4*["O"]:
                win(grille, ligne, jeton_joueur)
                return True

    #check vertical
    for element in range(colonne):
        # print("\n")
        for hauteur in range(ligne-3):
            check_lign = [grille[hauteur+i][element]for i in range(0,4)]
            # print("checklign"+str(check_lign))
            if check_lign == 4*["X"] or check_lign == 4*["O"]:
                win(grille, ligne, jeton_joueur)
                return True

def win(grille, ligne, jeton_joueur):
    affichage_grille (grille, ligne)
    print("\nGagné ! Joueur "+jeton_joueur)
    input()
    reinitialisation_grille(grille)

def draw(grille):
    print("\nEgalité !")
    input()
    reinitialisation_grille(grille)

def start(grille, ligne, colonne):
    gamemode = input("\nPVP  (1)\nSTOP (3)\n")
    if gamemode == "1" :
        while True :
            if placer_jeton("X", grille,ligne, colonne):
                break
            else :
                if placer_jeton("O", grille,ligne, colonne):
                    break
        start(grille, ligne, colonne)

    elif gamemode == "3":
        pass
    else:
        start(grille, ligne, colonne)


#Initiation du code
initialisation_grille(ligne,colonne,grille)
start(grille, ligne, colonne)
