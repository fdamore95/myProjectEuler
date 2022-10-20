# problem014

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

#%%

def process(n):
    count = 1
    while n>1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
        count += 1
    return count

#%%

def whichnumber(nmax):
    n = 1
    count = 0
    countmax = 0
    bestn = 1

    while n < nmax:
        count = process(n)
        if countmax < count:
            countmax = count
            bestn = n
        n += 1
    return (bestn, countmax)

#%%

nmax = 1000000
a= whichnumber(nmax)
print("n = {}, length = {}".format(a[0],a[1]))
# %%
