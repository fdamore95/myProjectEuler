# Problem 28
# ==========


#    Starting with the number 1 and moving to the right in a clockwise
#    direction a 5 by 5 spiral is formed as follows:

#                                  21 22 23 24 25
#                                  20  7  8  9 10
#                                  19  6  1  2 11
#                                  18  5  4  3 12
#                                  17 16 15 14 13

#    It can be verified that the sum of the numbers on the diagonals is 101.

#    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
#    formed in the same way?

import numpy as np
from numpy.core.defchararray import index

n = 1001

def main(n):
    moves = {
        1: [0,1],
        2: [1,0],
        3: [0,-1],
        4: [-1,0]
    }


    mat = np.zeros((n,n))

    cell = (n//2,n//2)

    starting_cell = cell

    number = 1

    index_move = 0

    move = moves[index_move + 1]

    mat[cell] = number

    number += 1

    while number < n**2 + 1:
        cell = (cell[0] + move[0], cell[1] + move[1])
        mat[cell] = number
        number += 1
        next_index_move = ((index_move + 1) % 4)
        next_move = moves[next_index_move + 1]
        next_cell = (cell[0] + next_move[0], cell[1] + next_move[1])
        if mat[next_cell] == 0:
            index_move = next_index_move
            move = next_move

    return int(np.trace(mat) + np.trace(np.flip(mat,axis = 1)) - mat[starting_cell])

print(main(n))