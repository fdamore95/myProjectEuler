# Problem 39
# ==========


#    If p is the perimeter of a right angle triangle with integral length
#    sides, {a,b,c}, there are exactly three solutions for p = 120.

#    {20,48,52}, {24,45,51}, {30,40,50}

#    For which value of p ≤ 1000, is the number of solutions maximised?

   
#    Answer: fa83a11a198d5a7f0bf77a1987bcd006

import tools

def compute_perimeter(a,b):
    return a + b + (a**2 + b**2)**0.5

def find_p(pmax):
    perims = [0 for _ in range(pmax + 1)]

    for a in range(1,int(pmax/3)):
        for b in range(a, int(pmax/2)):
            tmp = compute_perimeter(a,b)
            if tmp < pmax+1 and tmp - int(tmp) == 0:
                perims[int(tmp)] += 1
    return perims, tools.findmaxindex(perims)

maxp = 10**3
perims,p = find_p(maxp)
print(p)