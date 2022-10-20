# problem 3 STILL TO CORRECT

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

#%%

import numpy as np
import math

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

#%%
        

def largest_prime_factor(n):
    maximum = math.sqrt(n)
    prime_seq = eratosthenes(int(maximum))
    out = 1
    #print(prime_seq)
    while n > maximum:
        isprime = True
        for i in reversed(prime_seq):
            if n%i == 0:
                if i > out:
                    out = i
                n = n // i
                isprime = False
                while n%i == 0:
                    if i > out:
                        out = i
                    n = n // i
        if isprime == True:
            return n
    return out

#%%

n = 600851475143

print(largest_prime_factor(n))
# %%
