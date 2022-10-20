# Problem 32
# ==========


#    We shall say that an n-digit number is pandigital if it makes use of all
#    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
#    1 through 5 pandigital.

#    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
#    multiplicand, multiplier, and product is 1 through 9 pandigital.

#    Find the sum of all products whose multiplicand/multiplier/product
#    identity can be written as a 1 through 9 pandigital.

#    HINT: Some products can be obtained in more than one way so be sure to
#    only include it once in your sum.

import numpy as np

def is_pandigital_product(n):
    digits = [int(x) for x in list(str(n))]
    if len(set(digits)) < len(digits):
        return False
    max_div = int(n**0.5)
    for i in range(2,max_div + 1):
        remainder = n%i
        #print(f"Checking: {n}%{i} = {remainder}")
        if remainder == 0:
            #print(f"Divisor: {i}")
            j = n // i
            digits = [int(x) for x in list(str(i) + str(j) + str(n))]
            if len(set(digits)) == len(digits) and len(digits) == 9 and (0 not in digits):
                return True
    return False

def main():
    nmax = 99999 # we can't reach a 6-digits number as a product of two number with a total of 4 digits
    pangidits = []
    for n in range(1,nmax+1):
        if is_pandigital_product(n):
            pangidits += [n]
    
    return pangidits

print(np.sum(main()))
    


