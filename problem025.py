#%%

Fprev = 1
Fcurr = 1
count = 2

while Fcurr // 10**999 < 1:
    appo = Fcurr
    Fcurr += Fprev
    Fprev = appo
    count += 1

print(count)
# %%
