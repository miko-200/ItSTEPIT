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

input = input()
ns = input.split(' ')
n1 = int(ns[0])
n2 = int(ns[1])
print(int(n1), int(n2))
i = n1
while i < n2:
    if jePrvocislo(i) == True:
        print(i)
    i += 1