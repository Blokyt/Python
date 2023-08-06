from random import randint

def fillrandom(lenght, minvalue, maxvalue):
    i = 0
    list = []
    while i < lenght:
        list.append(randint(minvalue, maxvalue))
        i = i+1
    return list

lenght = 20
minvalue = 0
maxvalue = 10
A = fillrandom(lenght, minvalue, maxvalue)
print(A, "\n")

def trilist(list):
    Newlist = []
    i = 0
    longueur = len(list)
    while i < longueur:
        mini = list[0]
        k = 0
        while k < len(list):
            if list[k] < mini :
                mini = list[k]
            k = k+1
        list.remove(mini)
        Newlist.append(mini)
        i = i+1
    return Newlist

#NewA = trilist(A)
#print(NewA)
def selftrilist(list):
    longueur = len(list)
    i = 0
    while i < longueur:
        k = 0
        mini = list[0]
        while k < longueur-i:
            if list[k] < mini:
                mini = list[k]
            k = k+1
        list.append(mini)
        list.remove(mini)
        i = i+1
    return list

NewA = selftrilist(A)
print(NewA)
