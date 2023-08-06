import matplotlib.pyplot as plt
from math import *


def graphe(a,b,n=50):
    lx = [a+i/n for i in range((abs(a)+b)*n+1)]
    ly = [(cos(x)/x) for x in lx]
    plt.plot(lx,ly)

    ly = [(0) for x in lx]
    plt.plot(lx,ly)


    plt.show()  # affichage


# programme principal
graphe(1,-5)
