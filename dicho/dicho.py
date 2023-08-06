from random import randint
def createList(max, n):
    return [randint(0,max) for i in range(n)]

def SortList(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],list[j]
    return list

def dicho(list, target):)
    minIndex = 0
    maxIndex = len(list)-1
    currentIndex = (minIndex+maxIndex)//2
    while target != list[currentIndex] and minIndex < maxIndex:
        if target > list[currentIndex]:
            minIndex = currentIndex+1
        else:
            maxIndex = currentIndex-1
        currentIndex = (minIndex+maxIndex)//2
    if target == list[currentIndex]:
        return currentIndex, list[currentIndex]
    else:
        return str(target)+" n'est pas dans la liste",currentIndex, list[currentIndex]

max = 100
n = 100
target = 52

print(dicho(SortList(createList(max,n)),target))
