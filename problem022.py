#%%
mydict = dict()

for i in range(65,91):
    mydict[chr(i)] = i - 64

print(mydict)
# %%

import numpy as np

inpath = "p022_names.txt"

with open(inpath, 'r') as f:
    mynames = f.read()
    mynames = mynames.split(',')
    mynames = [x[1:len(x)-1] for x in mynames]

mynames = np.sort(mynames)

print(mynames)
# %%

position = 1
total_score = 0

for name in mynames:
    name_value = 0
    for x in name:
        name_value += mydict[x]
    name_value *= position
    total_score += name_value
    position +=1

print(total_score)

# %%
