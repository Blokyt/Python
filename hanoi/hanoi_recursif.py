def hanoi(n,deb,fin,inter):
    if n > 0:
        step += 1
        hanoi(n-1,deb,inter,fin)
        print(deb,"->",fin)
        hanoi(n-1,inter,fin,deb)
    return step


hanoi(3,"A","C","B")
