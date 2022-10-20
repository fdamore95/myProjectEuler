# Problem 33
# ==========


#    The fraction 49/98 is a curious fraction, as an inexperienced
#    mathematician in attempting to simplify it may incorrectly believe that
#    49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#    We shall consider fractions like, 30/50 = 3/5, to be trivial
#    examples.

#    There are exactly four non-trivial examples of this type of fraction, less
#    than one in value, and containing two digits in the numerator and
#    denominator.

#    If the product of these four fractions is given in its lowest common
#    terms, find the value of the denominator.

import math

def take_digits(n):
    return [int(x) for x in list(str(n))]

def copy_list(mylist):
    return [x for x in mylist]

def find_indeces(i,digits):
    indices = []
    count = 0
    for x in digits:
        if i == x:
            indices += [count]
        count += 1
    return indices

def number_from_digits(digits,len_digits):
    n = 0
    for i in range(len_digits):
        n += digits[i]*(10**(len_digits-1-i))
    return n

def is_good_fraction(n,m):
    if n % 10 == 0 or m % 10 == 0:
        return False
    digits_n = take_digits(n)
    digits_m = take_digits(m)
    n_len = len(digits_n)
    m_len = len(digits_m)
    for i in range(n_len):
        if digits_n[i] in digits_m:
            digits_n_copy = copy_list(digits_n)
            digits_n_copy.__delitem__(i)
            new_n = number_from_digits(digits_n_copy,n_len - 1)
            indices = find_indeces(digits_n[i],digits_m)
            for index in indices:
                digits_m_copy = copy_list(digits_m)
                digits_m_copy.__delitem__(index)
                new_m = number_from_digits(digits_m_copy,m_len - 1)
                if fraction_lct(new_n,new_m) == fraction_lct(n,m):
                    return True
    return False

def fraction_lct(n,m):
    gcd = math.gcd(n,m)
    n //= gcd
    m //= gcd
    return n,m

def main(nmax):
    good_fractions = []
    for n in range(11,nmax):
        for m in range(n + 1,nmax+1):
            if is_good_fraction(n,m):
                good_fractions += [[n,m]]
    num_fractions = len(good_fractions)
    num = 1
    den = 1
    for i in range(num_fractions):
        num *= good_fractions[i][0]
        den *= good_fractions[i][1]
    
    num,den = fraction_lct(num,den)

    #print(good_fractions)
    return den

nmax = 99
print(main(nmax))