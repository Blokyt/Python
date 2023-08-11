from random import randint
import sys
fichier = open("image.ppm", "w")
sys.stdout = fichier

def init_file(x, y, max=255, commentaire=""):
    print("P3")
    print("#", commentaire)
    print(x,y)
    print(max)

def pixel(x, y, max=255, deltacolor=255, colorchangerate=1):
    r = randint(0,max)
    g = randint(0, max)
    b = randint(0, max)
    for n in range(x*y):
        print(r, g, b)
        colorchange = randint(0,colorchangerate)
        if colorchange == 0:
            choosecolor = randint(0,2)
            if choosecolor == 0:
                b = randomize(b, max, deltacolor)
            elif choosecolor == 1:
                g = randomize(g,max, deltacolor)
            else:
                r = randomize(r,max, deltacolor)

def randomize(color, max, deltacolor):
    if color < deltacolor:
        newcolor =color + deltacolor
    elif color > max-deltacolor:
        newcolor = color - deltacolor
    else:
        if randint(0,1) == 1:
            newcolor = color + deltacolor
        else:
            newcolor = color - deltacolor
    return newcolor

x = 1000
y = 1000
max = 255
commentaire = ""
deltacolor = 1
colorchangerate = 1

init_file(x,y, max, deltacolor)

pixel(x, y, max, deltacolor, colorchangerate)

fichier.close()
