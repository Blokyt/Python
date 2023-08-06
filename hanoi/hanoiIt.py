def Hanoi(n):
    if n > 0:
        Hanoi(n-1)
    A = [n-i for i in range(n)]
    B, C = [], []
    Towers = [A,B,C]
    ShowTowers(Towers)

    countMove = 0

    if C != [n-i for i in range(n)]:
        Towers = MoveDisk1(Towers,n)
        ShowTowers(Towers)
        countMove += 1

    while C != [n-i for i in range(n)]:
        Towers = Move(Towers)
        ShowTowers([A,B,C])
        Towers = MoveDisk1(Towers,n)
        ShowTowers([A,B,C])
        countMove += 2
    print("n =",n,"-> ",countMove,"\n")

def MoveDisk1(Towers,n):
    for i in range(len(Towers)):
        if Towers[i] != [] and Towers[i][-1] == 1:
            if n%2 == 0:
                k = 1
            else:
                k = 5
            Towers[(i+k)%3].append(Towers[i].pop())
            return Towers

def Move(Towers):
    for i in range(len(Towers)):
        if Towers[i] != [] and Towers[i][-1] != 1:
            if (Towers[(i+1)%3] == [] or Towers[i][-1] < Towers[(i+1)%3][-1]):
                k = 1
            elif Towers[(i+5)%3] == [] or Towers[i][-1] < Towers[(i+5)%3][-1]:
                k = 5
            else:
                continue
            Towers[(i+k)%3].append(Towers[i].pop())
            return Towers

    return Towers


def ShowTowers(Towers):
    print(Towers)

Hanoi(int(input()))
