# Problem 67

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)


#%%

import numpy as np
#%%

def changetriangle(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    triangle = []
    for line in lines:
        array = np.array([int(x) for x in line.split(" ")])
        triangle.append(array)
    triangle = np.array(triangle)
    sizetriangle = len(triangle)
    for i in range(sizetriangle-1,0,-1):
        for j in range(0,i):
            newnum = max(triangle[i][j], triangle[i][j+1])
            triangle[i-1][j] += newnum
    return triangle[0][0]

#%%

path = './problem067.txt'

print('{}\n'.format(changetriangle(path)))
# %%

# %%
