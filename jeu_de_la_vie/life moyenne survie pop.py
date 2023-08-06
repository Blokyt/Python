from random import randint
from colored import *
cyan = fg('cyan')
reset = attr('reset')

def print_tableau():
    for i in range(x):
        for j in range(y):
            if tableau[j][i] == 1:
                print(cyan+"<>"+reset, end="")
            else:
                print("  ", end="")
        print("")

def config_init(x,y):
    mode = input("1 : lancer simulation\n2 : configurer\n3 : config random\n")
    if mode == "1":
        pass
    elif mode == "2":
        i = int(input("x : "))
        j = int(input("y : "))
        tableau[j][i]=1
        config_init(x, y)
    else:
        for i in range(0,x):
            for j in range(0, y):
                luck = randint(1,2)
                if luck == 1:
                    tableau[j][i] = 1

def simulation(x,y,tableau):
    sum = 0
    new_tableau = [[0 for i in range (x)] for j in range (y)]
    for i in range(1,x-1):
        for j in range(1, y-1):
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    sum += tableau[j+k][i+l]
            sum -= tableau[j][i]
            if tableau[j][i] == 0:
                if sum == 3 :
                    new_tableau[j][i] = 1
            else :
                if sum in [2,3]:
                    new_tableau[j][i] = 1
                else:
                    new_tableau[j][i] = 0
            sum = 0
    return new_tableau

def prog():
    x = int(input("x : "))
    y = int(input("y : "))

    n = int(input("Repetition : "))
    sum = 0
    for k in range(n):
        tableau = [[0 for i in range (x)] for j in range (y)]
        #config_init(x, y)
        for i in range(0,x):
            for j in range(0, y):
                luck = randint(1,2)
                if luck == 1:
                    tableau[j][i] = 1
        i = 0
        tPREV1 = []
        tPREV2 = []
        tPREV3 = []
        tPREV4 = []
        while not tableau in [tPREV1, tPREV2, tPREV3, tPREV4] and i <= x*y*2+26:
            #if i > x*y*2:
                #print_tableau()
            i += 1
            #print(i)
            #input()
            tPREV4 = tPREV3
            tPREV3 = tPREV2
            tPREV2 = tPREV1
            tPREV1 = tableau

            tableau = simulation(x,y,tableau)
        sum += i
        #print(k+1)
        #print(sum)
    moyenne = sum/n
    print("La temps de survie moyen d'une population ", x, y,"est de ",moyenne)
    
while True:
    prog()
    input()
