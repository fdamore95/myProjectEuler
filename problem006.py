# Problem 6

# The sum of the squares of the first ten natural numbers is 385

# The square of the sum of the first ten natural numbers is 55^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#%%

import numpy as np

def main(n):
    tosum = np.array(range(1,n+1))
    squaresum = sum(tosum)**2
    sumofsquares = 0
    for i in tosum:
        sumofsquares += i**2
    return -sumofsquares+squaresum

def fastmain(n):
    squaresum = int((n*(n+1)/2)**2)
    sumofsquares = int(n*(n+1)*(2*n+1)/6)
    return squaresum-sumofsquares

# %%

n = 100

print(main(n))

print(fastmain(n))

# %%
