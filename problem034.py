# Problem 34
# ==========


#    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#    Find the sum of all numbers which are equal to the sum of the factorial of
#    their digits.

#    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import math

def is_sum_of_digit_fact(n):
    digits = [int(x) for x in list(str(n))]
    mysum = 0
    for x in digits:
        mysum += math.factorial(x)
        if mysum > n:
            return False
    if mysum == n:
        return True
    else:
        return False

def main(n):
    mysum = 0
    for x in range(10,n+1):
        if is_sum_of_digit_fact(x):
            mysum += x
    return mysum

n = 2903040 
# this is the max number to check
# indeed, of each m >= n, the sum of the factorial of the digits of m is less than m

print(main(n))



