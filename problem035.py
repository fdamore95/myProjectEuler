# Problem 35
# ==========


#    The number, 197, is called a circular prime because all rotations of the
#    digits: 197, 971, and 719, are themselves prime.

#    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
#    71, 73, 79, and 97.

#    How many circular primes are there below one million?

import tools

def shift_list(mylist):
    newlist = [x for x in mylist[1:]]
    newlist += [mylist[0]]
    return newlist

def is_circular(x,primes):
    digits = tools.extract_digits(x)
    len_digits = len(digits)
    for _ in range(len_digits):
        num = tools.number_from_digits(digits)
        if num not in primes:
            return False
        digits = shift_list(digits)
    return True

def main(n):
    primes = tools.eratosthenes(n)
    num_primes = len(primes)
    count = 0
    for i in range(num_primes):
        if is_circular(primes[i],primes):
            count += 1
    return count

n = 10**6
print(main(n))            


