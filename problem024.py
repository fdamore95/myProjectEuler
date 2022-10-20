#%%

n = 10

#n = 3

mydigits = list(range(n))


#%%

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

#%%

#print(permutation(mydigits))

print(permutation(mydigits)[10**6-1])
# %%
