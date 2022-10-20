#%%
#
# 

import numpy as np

n = 100

myfact = 1

for i in range(n):
    myfact *= i+1

print(f"{n}! = {myfact}")
# %%

sum = 0

while myfact > 0:
    sum += np.mod(myfact,10)
    myfact = myfact // 10

print(f"The sum of the digits is {sum}")
# %%
