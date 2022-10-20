
#%%
def eucl_division(m,n): # m / n
    return [m//n, m%n]


def get_decimal_part(n):
    decimal_part = []
    div_results = []
    appo = eucl_division(1,n)
    while not appo in div_results:
        div_results += [appo]
        decimal_part += [appo[0]]
        if appo[1] == 0:
            break
        appo = eucl_division(appo[1]*10,n)
    
    count = 0
    for pair in div_results:
        if appo == pair:
            break
        count += 1
    
    period = decimal_part[count:]
    return decimal_part,period

def get_period(n):
    return get_decimal_part(n)[1]

n = 1000
len_max_period = 0
winner = 0

for i in range(2,n):
    appo = len(get_period(i))
    if appo > len_max_period:
        len_max_period = appo
        winner = i

print(winner)



# %%
