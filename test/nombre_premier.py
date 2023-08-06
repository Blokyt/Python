
def nombre_pre(x):
    som_div = 1
    for div in range(2,x):
        if (x % div) == 0:
            som_div = som_div + div
    return som_div

def is_prime(x):
    return nombre_pre(x) == 1

def all_primeInRangeOf(n, primes):
    count = 0
    for x in range(2, n):
        if is_prime(x):
            primes.append(x)
            count += 1
    #print("total : "+str(count))





def decomp(x):
    primes = []
    all_primeInRangeOf(x, primes)
    decomp = []
    for div in primes:
        n = x
        while n % div == 0:
            n = n/div
            decomp.append(str(div))
    #print("Decomposition en facteur premier de "+str(x)+" : "+str(decomp))
    return decomp

def decompInRangeOf(n):
    if n - int(n) == 0.5:
        print(str(int(n-0.5))+str(decomp(int(n-0.5))))
    else:
        for x in range(10**3*int(n),10**3*int(n)+1000+1 ):
            print(str(x)+str(decomp(x)))
    decompInRangeOf(int(input()))

decompInRangeOf(float(input()))
