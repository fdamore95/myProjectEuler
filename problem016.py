# problem016

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

#%%

def main(n):
    number = 2**n
    string = str(number)
    #string = string.split("")
    return sum(list(map(int,string)))

#%%

n = 1000
print(main(n))
# %%
