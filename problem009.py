# problem 9

#%%

import math
#%%

def findtriplet(n):
    if n<1:
        print("n must be bigger")
        exit()
    for b in range(1,int(math.ceil(n/2)+1)):
        for a in range(0,b+1):
            test = math.sqrt(a**2+b**2)
            if test.is_integer() and a + b + int(test) == n:
                return [a,b,int(test)] 
    print("no triplet found")
    exit()

#%%

def main(n):
    a = findtriplet(n)
    out = 1
    for i in a:
        out *= i
    return out   

#%%

n = 1000
print(main(n))
# %%
