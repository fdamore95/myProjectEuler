# Problem 30
# ==========


#    Surprisingly there are only three numbers that can be written as the sum
#    of fourth powers of their digits:

#      1634 = 1^4 + 6^4 + 3^4 + 4^4
#      8208 = 8^4 + 2^4 + 0^4 + 8^4
#      9474 = 9^4 + 4^4 + 7^4 + 4^4

#    As 1 = 1^4 is not a sum it is not included.

#    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#    Find the sum of all the numbers that can be written as the sum of fifth
#    powers of their digits.

import numpy as np

def main(myexp):
    nmax = 1
    maxsum = 9**myexp
    while maxsum > nmax:
        nmax *= 10
        maxsum += 9**myexp

    numbers = []
    
    for n in range(2,nmax+1):
        digits = [int(x) for x in list(str(n))]
        inner_sum = 0
        for x in digits:
            inner_sum += x**myexp
        if n == inner_sum:
            numbers += [n]
    
    return np.sum(numbers)

myexp = 5
print(main(myexp))