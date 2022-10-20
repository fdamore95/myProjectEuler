# Problem 38
# ==========


#    Take the number 192 and multiply it by each of 1, 2, and 3:

#      192 × 1 = 192
#      192 × 2 = 384
#      192 × 3 = 576

#    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
#    will call 192384576 the concatenated product of 192 and (1,2,3)

#    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
#    and 5, giving the pandigital, 918273645, which is the concatenated product
#    of 9 and (1,2,3,4,5).

#    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
#    the concatenated product of an integer with (1,2, ... , n) where n > 1?

   
#    Answer: f2a29ede8dc9fae7926dc7a4357ac25e

import tools 

def create_pans(digits):
    pans = tools.permutation(digits)
    for i in range(len(pans)):
        pans[i] = tools.number_from_digits(tools.extract_digits(pans[i]))
    return sorted(pans)[::-1]

def concatenated_prod(n,mylist):
    prods = []
    for i in mylist:
        prods += [n*i]
    return tools.concatenate_numbers(prods)


def main():
    all_digits = list(range(1,10))
    pans = create_pans(all_digits)
    n = max(pans)
    found = 1
    test = 1
    mylist = list(range(1,15)) # 15! is greater than 10^9
    '''
    10^3 is enough because already surpasses 10^9
    with the conc prod by (1,2)
    '''
    while test < 10001: # 
        list_ind = 1
        myprod = concatenated_prod(test,mylist[:list_ind])
        while myprod < n + 1:
            if tools.is_pandigital(myprod,all_digits) and myprod > found:
                found = myprod
            list_ind += 1
            myprod = concatenated_prod(test,mylist[:list_ind])
        test += 1
    return found


print(main())