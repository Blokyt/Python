from math import sqrt
import matplotlib.pyplot as plt

V = [21,26,31,36,41,46,51,56]
UV = 1
p = [1860,1525,1300,1115,1002,870,789,726]
Up = 1

def U(V,p,UV,Up):
    return round(p*(10**2)*V*(10**-6)*sqrt((Up/p)**2+(UV/V)**2),2)

for i in range(len(V)):
    print(f"U({p[i]}*{V[i]}) = ( {p[i]}*10² * {V[i]}*10^-6* √(( {Up} / {p[i]} )² + ( {UV} / {V[i]} )²) = {U(V[i],p[i],UV,Up)}")

plt.plot([1/v for v in V],p)
plt.show()
