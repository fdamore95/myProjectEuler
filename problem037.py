# Problem 37
# ==========


#    The number 3797 has an interesting property. Being prime itself, it is
#    possible to continuously remove digits from left to right, and remain
#    prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
#    right to left: 3797, 379, 37, and 3.

#    Find the sum of the only eleven primes that are both truncatable from left
#    to right and right to left.

#    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import tools

def truncate_from_left(n):
    digits = tools.extract_digits(n)
    return tools.number_from_digits(digits[1:])

def truncate_from_right(n):
    digits = tools.extract_digits(n)
    return tools.number_from_digits(digits[:-1])

def is_truncatable(primes, n):
    tmp = n
    while n > 9:
        if n not in primes:
            return False
        else:
            n = truncate_from_left(n)
    if n not in primes:
        return False
    n = tmp
    while n > 9:
        if n not in primes:
            return False
        else:
            n = truncate_from_right(n)
    if n not in primes:
        return False
    return True

def main(nmax,maxcount):
    primes = tools.eratosthenes(nmax)
    count = 0
    mysum = 0
    num_primes = len(primes)
    for n in range(num_primes):
        if primes[n] > 7 and is_truncatable(primes,primes[n]):
            mysum += primes[n]
            count += 1
        if count == maxcount:
            break
    return mysum, count, n, num_primes

nmax = 10**6
maxcount = 11

print(main(nmax,maxcount))




