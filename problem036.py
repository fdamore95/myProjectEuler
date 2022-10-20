# Problem 36
# ==========


#    The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
#    bases.

#    Find the sum of all numbers, less than one million, which are palindromic
#    in base 10 and base 2.

#    (Please note that the palindromic number, in either base, may not include
#    leading zeros.)

import tools

def main(base,nmax):
    mysum = 0
    for n in range(1,nmax):
        if tools.is_palindromic(n) and tools.is_palindromic(tools.decimal_to_base(n,base)):
            mysum += n
    return mysum

base = 2
nmax = 10**6
print(main(base,nmax))