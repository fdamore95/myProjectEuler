#%%

import numpy as np

n = 10000

mypairs = np.zeros((n,2),dtype = int)
for k in range(0,n):
    sum = 0
    for i in range(1,k+1):
        if (k+1)%i == 0:
            sum += i
    mypairs[k,0] = k+1
    mypairs[k,1] = sum

sum_amicable = 0
done = []
amicable_pairs = []

for k in range(n):
    done += [k+1]
    appo = mypairs[k,1]
    if appo < n + 1 and mypairs[appo - 1, 1] == k+1 and not appo in done:
        sum_amicable += appo + k+1
        amicable_pairs += [[k+1,appo]]

print(sum_amicable)
print(amicable_pairs)


# %%
