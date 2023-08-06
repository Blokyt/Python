from random import randint



xpos = 0
ypos = 0

maze = []

def init_maze(x, y):
    #initialisation du maze
    for n in range(x):
        maze.append(y*["x"])

def show_maze():
    #affichage du maze ligne par ligne
    for line in maze:
        print(line)
    print("\n")

def gen_maze(x, y, ypos, xpos, dx=0, dy=0):
        #decalage en ordonée
        dy = randint(-ypos, (x-1)-ypos)
        print("dy "+str(dy))
        if dy < 0:
            for i in range(0, -dy+1):
                maze[ypos-i][xpos+dx] = "-"
        else:
            for i in range(0, dy+1):
                maze[ypos+i][xpos+dx] = "-"

            #update de la position
        xpos = xpos+dx
        print("xpos "+str(xpos))
        ypos = ypos+dy
        print("ypos "+str(ypos))

        #decalage en abscisse
        dx = randint(-xpos, (x-1)-xpos)
        print("dx "+str(dx))
        if dx < 0:
            for i in range(0, -dx+1):
                maze[ypos][xpos-i] = "-"
        else:
            for i in range(0, dx+1):
                maze[ypos][xpos+i] = "-"

                #update de la position
        xpos = xpos+dx
        print("xpos "+str(xpos))
        ypos = ypos
        print("ypos "+str(ypos))

        if ypos != (x-1):
            gen_maze(x, y, ypos, xpos)
        else:
            while True :
                ny = 0
                for line in maze:
                    ny = ny+1
                    nx = 0
                    for elem in line:
                        nx = nx+1
                        if elem == "-" and ny > y/2 and randint(0, x**3) == 1:
                            maze[ny-1][nx-1]= "o"
                            return



def create_maze(x, y, maze=maze):
    #affectation des variables | le -2 compense l'ajout des bordure au formatage
    x = x - 2
    y = y - 2
    #initialisation du maze
    init_maze(x, y)

    #generation du maze avec dx_init comme valeur de départ
    dx_init = randint(0, x-1)
    dx_init = 0
    print("dx init "+str(dx_init)+"\n")

    gen_maze(x, y, ypos, xpos, dx_init)

    #affichage du maze
    #show_maze()

    #formatage du maze et encodage en .txt et recompensation des x et y
    #x = x+2
    maze = [x*"x"]+maze+[x*"x"]
    with open("maze.txt", 'w') as f:
        for ligne in maze:
            #y = y+2
            f.write(str("x"+"".join(ligne)+"x") + '\n')
    with open("maze.txt", 'r') as f:
        maze = [line.rstrip('\n') for line in f]

#create_maze(x colonnes, y lignes)
create_maze(50, 50)
