import random, math

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

numsF = []
print("CISLO                            FAKTORIZACIA")
nOfNs = random.randint(1, 20)
for i in range(nOfNs):
    numsF = []
    rNum = random.randint(2, 10**2)
    num = rNum
    while num > 1:
        maxN = 2
        for j in range(num):
            jP = jePrvocislo(j)
            if jP == True and j > maxN and (num%j == 0):
                maxN = j
        numsF.append(maxN)
        num = int(num / maxN)
    numsF.sort()
    nums = ""
    for f in range(len(numsF)):
        if f == 0:
            nums = str(numsF[f])
        else:
            nums += " x " + str(numsF[f])
    print(rNum, " = ", nums)
