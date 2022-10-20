# problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

#%%

import numpy as np
import math

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

def main(n):
    if n < 56:
        x = n**2
        prime_seq = eratosthenes(x)
    else:
        x = 2*n*math.log(n)
        x = int(math.ceil(x))
        prime_seq = eratosthenes(x)
    return prime_seq[n-1]

#%%

n = 10001
print(main(n))

# %%
