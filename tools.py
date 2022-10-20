import numpy as np

def key_from_value(mydict,value):
    pairs = mydict.items()
    pairs_len = len(pairs)
    for i in range(pairs_len):
        if value == pairs[i][1]:
            return pairs[i][0]
    ValueError("No key corresponding to the given value.")

def eratosthenes(n):
    prime_seq = list(range(n+1))
    prime_seq[0:2] = [0,0]
    tokeep = [2]

    maxit = np.sqrt(n)+1

    index = 2**2
    while index < n+1:
        prime_seq[index] = 0
        index +=2

    for i in range(3,n+1):
        if prime_seq[i] > 0 and i < maxit:
            index = i**2
            while index < n+1:
                prime_seq[index] = 0
                index += 2*i
            tokeep += [i]
        elif prime_seq[i]>0:
            tokeep += [i]
    return np.array(prime_seq)[tokeep]

def extract_digits(x):
    return [int(y) for y in list(str(x))]

def extract_digits_as_str(x):
    return [y for y in list(str(x))]


def number_from_digits(digits):
    len_num = len(digits)
    count = 0
    num = 0
    for x in digits:
        x = int(x)
        num += x*(10**(len_num - 1 - count))
        count += 1
    return num

DIGITS = {0: "0",1: "1",2: "2",3: "3",4: "4",5: "5",6: "6",7: "7",8: "8",9: "9",10: "A",11: "B",12: "C",13: "D",14: "E",15: "F",16: "G",17: "H",18: "I",19: "J",20: "K",21: "L",22: "M",23: "N",24: "O",25: "P",26: "Q",27: "R",28: "S",29: "T",30: "U",31: "V",32: "W",33: "X",34: "Y",35: "Z"}

def decimal_to_base(n,base):
    if n == 0:
        return 0
    digits = []
    while n > 0:
        remainder = n % base
        digits.append(f"{DIGITS[remainder]}")
        n //= base
    if base < 11:
        digits = [int(x) for x in digits]
        return number_from_digits(digits[::-1])
    else:
        num_str = ""
        for x in digits[::-1]:
            num_str += x
        return num_str

def base_to_decimal(n,base):
    n = str(n)
    digits = [key_from_value(DIGITS,x) for x in list(str(n))]
    count = 0
    n_decimal = 0
    for x in digits:
        n_decimal += x*(base**count)
        count += 1
    return n_decimal

def base_to_base(n,start_base,end_base):
    return (decimal_to_base(base_to_decimal(n,start_base),end_base))

def concatenate_numbers(numbers):
    digits = []
    for n in numbers:
        digits += extract_digits(n)
    return number_from_digits(digits)

def is_palindromic(n):
    digits = extract_digits_as_str(n)
    if digits == digits[::-1]:
        return True
    return False

def is_pandigital(n,all_digits):
    digits = extract_digits(n)
    if not len(digits) == len(all_digits):
        return False
    for i in all_digits:
        if i not in digits:
            return False
    return True

def permutation(lst):
    if len(lst) == 0:
        raise Exception("the list must have length at least 1")
    if len(lst) == 1:
        return [lst[0]]
    all_perm = []
    num_elements = len(lst)
    for i in range(num_elements):
        m = lst[i]*10**(num_elements-1)
        remlst = lst[:i] + lst[i+1:]
        for p in permutation(remlst):
            #print(p)
            all_perm.append(m+p)
    return all_perm

def findmax(mylst):
    tmp = mylst[0]
    for x in mylst[1:]:
        if tmp < x:
            tmp = x
    return tmp

def findmaxindex(mylst):
    tmpmax = mylst[0]
    tmpindex = 0
    count = 0
    for x in mylst[1:]:
        count += 1
        if tmpmax < x:
            tmpmax = x
            tmpindex = count
    return tmpindex