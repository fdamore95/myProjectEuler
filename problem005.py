# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#%%

import numpy as np

#%%


def eratosthenes(n):
    prime_seq = list(range(n+1))
    prime_seq[0:2] = [0,0]
    tokeep = [2]

    maxit = np.sqrt(n)+1

    index = 2**2
    while index < n+1:
        prime_seq[index] = 0
        index +=2

    for i in range(3,n+1):
        if prime_seq[i] > 0 and i < maxit:
            index = i**2
            while index < n+1:
                prime_seq[index] = 0
                index += 2*i
            tokeep += [i]
        elif prime_seq[i]>0:
            tokeep += [i]
    return np.array(prime_seq)[tokeep]

##

def decompose(n, prime_seq):
    decomposition = list()
    # println(prime_seq)
    for i in prime_seq:
        if i <= n:
            # println(i)
            factor = 0
            while n%i == 0:
                n = int(n/i)
                factor += 1
            #print(factor)
            if factor>0:
                decomposition.append([i, factor])
        else:
            break        
    return decomposition

##

def main(n):
    if n < 1:
        print("the input n = {} must be greater than 0".format(n))
        exit()
    mcm = 1
    prime_seq = np.array(eratosthenes(n))
    #print(prime_seq)
    for i in range(2,n+1):
        factors = np.array(decompose(i,prime_seq))
        #print(factors)
        count = 0
        for j in factors[:,0]:
            support = mcm
            for k in range(1,factors[count,1]+1):
                if support%j == 0:
                    support /= j
                else:
                    mcm *= j
            count +=1
    return mcm

n = 20
mcm = main(n)
print(mcm)

# %% fast way to do it

np.lcm.reduce(np.array(range(1,n+1)))
# %%
