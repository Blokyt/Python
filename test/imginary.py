from math import *

def realToimgForm(real, imaginary):
    r = sqrt(real**2+imaginary**2)
    teta = acos(real/r)
    img = r*e**(1j*teta)

    img2 = str(r)+"e^i"+str(teta)
    return img, img2



print(realToimgForm(34, 0.33))
