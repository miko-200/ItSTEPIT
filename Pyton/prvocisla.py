import random
import math

def jePrvocislo(n):
    i = 1
    while i <= (math.sqrt(n)):
        if i == 1:
            i += 1
            continue
        elif (n%i) == 0:
            return False
        i += 1
    return True

print("CISLO                            JE PRVOCISLO")
nOfNs = random.randint(1, 20)
for i in  range(nOfNs):
    n  = random.randint(1, 10**2)
    jeP = jePrvocislo(n)
    p= ""
    if jeP == True:
        p = "ANO"
    else:
        p = "NIE"
    print(n, "          ", p)