#%% 

import time

start_time = time.time()

#n = 28123
n=28

abundant_numbers = []

for i in range(1,n):
    if not i in abundant_numbers:
        mysum = 0
        for j in range(2,int(i**0.5)):
            if i%j == 0:
                mysum += j
                print(i,j,i//j)
                if j**2 != i:
                    mysum += i//j
            mysum += 1
        if mysum >= i:
            if mysum > i:
                if not i in abundant_numbers:
                    abundant_numbers+=[i]
            for k in range(2,int(n/i)+1):
                appo = k*i
                if not appo in abundant_numbers and appo < n:
                    abundant_numbers += [appo]


#%%

sum_of_abundant_numbers = set()

for i in abundant_numbers:
    for j in abundant_numbers:
        sum_of_abundant_numbers.add(i + j)



#%%


mysum = int((n-1)*n/2)

for x in sum_of_abundant_numbers:
    if x < n:
        mysum -= x

print(mysum, "in time ", time.time()-start_time)
# %%
