# Problem 31
# ==========


#    In England the currency is made up of pound, £, and pence, p, and there
#    are eight coins in general circulation:

#      1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

#    It is possible to make £2 in the following way:

#      1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

#    How many different ways can £2 be made using any number of coins?

## trying recursive

MYCOINS = [1,2,5,10,20,50,100,200]
NUMCOINS = len(MYCOINS)


def main(n,maxcoin_index):
    if n == 0:
        return [[]]
    elif n == 1:
        return [[1]]
    else:
        combinations = []
        for i in range(maxcoin_index,-1,-1):
            x = MYCOINS[i]
            if  x < n + 1:
                inner_combs = main(n-x,i)
                for inner_comb in inner_combs:  
                    comb = [x] + inner_comb
                    combinations += [comb]
        return combinations

# def delete_repeated_combs(combinations):
#     combinations = [sorted(x) for x in combinations]
#     combinations = sorted(combinations)
#     all_combs = len(combinations)
#     i = 0
#     while i < all_combs - 1:
#         while combinations[i] == combinations[i+1]:
#             combinations.__delitem__(i+1)
#             all_combs -= 1
#             if i+1 > all_combs -1:
#                 break
#         i += 1
#     return combinations


n = 200
combinations = main(n,NUMCOINS-1)
print(len(combinations))

