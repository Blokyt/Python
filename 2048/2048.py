from random import randint

def afficheTableau():
    i = 0
    while i < len(tableau):
        print(tableau[i])
        i += 1
    print("")


def spawnRandom():
    x = randint(0,xline-1)
    y = randint(0,yline-1)
    while tableau[y][x] != 0:
        x = randint(0,xline-1)
        y = randint(0,yline-1)
    tableau[y][x] = 2**(randint(SpawnPuissanceMin, SpawnPuissanceMax))

def moveup():
    n = 0
    for y in range(1,yline):
        for x in range(xline):
            if tableau[y][x] != 0 :
                i = 1
                # addition des nombres similaire vers le haut
                while i <= y and (tableau[y-i][x] == 0 or tableau[y-i][x] == tableau[y][x]):
                    if tableau[y][x] == tableau[y-i][x]:
                        tableau[y-i][x] = tableau[y-i][x]*2
                        tableau[y][x] = 0
                        n += 1
                    i += 1
                i = 1
                # plaquement des nombres vers le haut
                while i <= y and tableau[y-i][x] == 0:
                    i +=1
                temp = tableau[y][x]
                tableau[y][x] = 0
                tableau[y-i+1][x] = temp
                if i > 1:
                    n += 1
    return n

def movedown():
    n = 0
    for y in range(yline-2,-1,-1):
        for x in range(xline):
            if tableau[y][x] != 0 :
                i = 1
                # addition des nombres similaire vers le bas
                while i <= yline-1-y and (tableau[y+i][x] == 0 or tableau[y+i][x] == tableau[y][x]):
                    if tableau[y][x] == tableau[y+i][x]:
                        tableau[y+i][x] = tableau[y+i][x]*2
                        tableau[y][x] = 0
                        n += 1
                    i += 1
                i = 1
                # plaquement des nombres vers le bas
                while i <= yline-1-y and tableau[y+i][x] == 0:
                    i +=1
                temp = tableau[y][x]
                tableau[y][x] = 0
                tableau[y+i-1][x] = temp
                if i > 1:
                    n += 1
    return n

def moveleft():
    n = 0
    for y in range(yline):
        for x in range(1,xline):
            if tableau[y][x] != 0 :
                i = 1
                # addition des nombres similaire vers la gauche
                while i <= x and (tableau[y][x-i] == 0 or tableau[y][x-i] == tableau[y][x]):
                    if tableau[y][x] == tableau[y][x-i]:
                        tableau[y][x-i] = tableau[y][x-i]*2
                        tableau[y][x] = 0
                        n += 1
                    i += 1
                i = 1
                # plaquement des nombres vers le gauche
                while i <= x and tableau[y][x-i] == 0:
                    i +=1
                temp = tableau[y][x]
                tableau[y][x] = 0
                tableau[y][x-i+1] = temp
                if i > 1:
                    n += 1
    return n

def moveright():
    n = 0 #compteur de mouvement
    for y in range(yline):
        for x in range(xline-2,-1,-1):
            if tableau[y][x] != 0 :
                i = 1
                # addition des nombres similaire vers la droite
                while i <= xline-1-x and (tableau[y][x+i] == 0 or tableau[y][x+i] == tableau[y][x]):
                    if tableau[y][x] == tableau[y][x+i]:
                        tableau[y][x+i] = tableau[y][x+i]*2
                        tableau[y][x] = 0
                        n += 1
                    i += 1
            if tableau[y][x] != 0 :
                i = 1
                # plaquement des nombres vers la droite
                while i <= xline-1-x and tableau[y][x+i] == 0:
                    i +=1
                temp = tableau[y][x]
                tableau[y][x] = 0
                tableau[y][x+i-1] = temp
                if i > 1:
                    n += 1
    return n

def VerifEnd():
    for line in tableau:
        for elem in line:
            if elem == 0:
                return False
    for y in range(yline):
        for x in range(xline):
            if y == 0:
                if x == 0:
                    if tableau[y][x] in [tableau[y+1][x], tableau[y][x+1]]:
                        return False
                elif x == xline-1:
                    if tableau[y][x] in [tableau[y+1][x], tableau[y][x-1]]:
                        return False
                else:
                    if tableau[y][x] in [tableau[y+1][x], tableau[y][x+1], tableau[y][x-1]]:
                        return False
            elif y == yline-1 :
                if x == 0:
                    if tableau[y][x] in [tableau[y-1][x], tableau[y][x+1]]:
                        return False
                elif x == xline-1:
                    if tableau[y][x] in [tableau[y-1][x], tableau[y][x-1]]:
                        return False
                else:
                    if tableau[y][x] in [tableau[y-1][x], tableau[y][x+1], tableau[y][x-1]]:
                        return False
            elif x == 0:
                if tableau[y][x] in [tableau[y+1][x], tableau[y-1][x], tableau[y][x+1]]:
                    return False
            elif x == xline-1:
                if tableau[y][x] in [tableau[y+1][x], tableau[y-1][x], tableau[y][x-1]]:
                    return False
            else:
                if tableau[y][x] in [tableau[y+1][x], tableau[y-1][x], tableau[y][x-1], tableau[y][x+1]]:
                    return False
    return True


SpawnPuissanceMin = 1
SpawnPuissanceMax = 2
xline = 5
yline = 5
tableau = [[0 for y in range(xline)] for x in range(yline)]
maximumelem = 0
k = 0
while maximumelem < 2048:
    k +=1
    print(k)
    tableau = [[0 for y in range(xline)] for x in range(yline)]
    spawnRandom()
    #afficheTableau()
    while not VerifEnd() :
        move = None#input("up / down / left / right : ")
        ia = randint(1,4)
        #print("")
        if move == "up" or ia == 1:
            n = moveup()
        elif move == "down" or ia == 2:
            n = movedown()
        elif move == "left" or ia == 3:
            n = moveleft()
        elif move == "right" or ia == 4:
            n = moveright()
        else:
            continue
        if n > 0:
            #afficheTableau()
            spawnRandom()
            #afficheTableau()
    #afficheTableau()
    for line in tableau:
        for elem in line:
            if elem > maximumelem:
                maximumelem = elem
    #print(maximumelem)
afficheTableau()
print(maximumelem)
