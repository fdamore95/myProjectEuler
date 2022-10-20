#%%

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)):
        if n%i == 0:
            return False
    return True

amax = 1000
bmax = 1000

max_num_of_consecutive_primes = 0
best_a = 0
best_b = 0
#isprime = True

for a in range(-amax+1, amax):
    for b in range(2,bmax+1):
        n = 0
        num_of_consecutive_primes = 0 
        isprime = is_prime(n**2 + a*n + b)
        while isprime:
            num_of_consecutive_primes += 1
            n+=1
            isprime = is_prime(n**2 + a*n + b)
        if num_of_consecutive_primes > max_num_of_consecutive_primes:
            max_num_of_consecutive_primes = num_of_consecutive_primes
            best_a = a
            best_b = b


print(best_a*best_b)
print(max_num_of_consecutive_primes)
        


# %%
