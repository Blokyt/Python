from random import randint

def createList(max, n):
    return [randint(0,max) for i in range(n)]

def SortList(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],list[j]
    return list

def dichoRecursion(list, target, minIndex, maxIndex):
    currentIndex = (minIndex+maxIndex)//2
    if target == list[currentIndex]:
        return currentIndex, list[currentIndex]
    elif not minIndex < maxIndex:
        return str(target)+" n'est pas dans la liste",currentIndex, list[currentIndex]
    elif target > list[currentIndex]:
        return dichoRecursion(list, target, currentIndex+1, maxIndex)
    else:
        return dichoRecursion(list, target, minIndex, currentIndex-1)

max = 100
n = 10
target = 12
list = SortList(createList(max,n))
print(dichoRecursion(list, target, 0,len(list)-1))
