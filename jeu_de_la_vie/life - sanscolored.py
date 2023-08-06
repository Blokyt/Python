from random import randint

x = 10
y = 10

tableau = [[0 for i in range (x)] for j in range (y)]

def print_tableau():
    for i in range(x):
        for j in range(y):
            if tableau[j][i] == 1:
                print("<>", end="")
            else:
                print("  ", end="")
        print("")

def config_init(x,y):
    mode = input("1 : lancer simulation\n2 : configurer\n3 : config random\n\n")
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
    print("\n")


def simulation():
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


config_init(x, y)

i = 0
while True:
    print_tableau()
    i += 1
    print(i)
    input()
    tableau = simulation()
