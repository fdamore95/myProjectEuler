# problem 4



# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


#%%

import numpy as np

def verify_palindrome(n):
    digits = []
    while n>0:
        digits += [n%10]
        n = int(n/10)
    # print(digits)
    if list(digits) == list(reversed(digits)):
        return True
    else:
        return False

def get_number():
    max = 0
    for i in range(999,99,-1):
        for j in range(i, 99, -1):
            if i*j < max:
                break
            #print(i,j)
            n = i*j
            if verify_palindrome(n):
                if max < n:
                    max = n
    return max
                

#print(verify_palindrome(1001))

print(get_number())

# %%
