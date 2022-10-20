# problem10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

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

#%%

def isprime(n,tests):
    for i in tests:
        if i > math.sqrt(n):
            break
        if n % i == 0:
            return False
    return True

#%%

def main(n):
    tests = eratosthenes(int(math.floor(n)))
    out = 0
    for i in tests:
        out += i
    for j in range(i+1,n+1):
        # if j%10000 == 0:
        #    print(j)
        if j%2 == 1:
            if isprime(j,tests):
                out +=j
    return out

#%%

n = 2*10**6

print(main(n))
    
# %%
