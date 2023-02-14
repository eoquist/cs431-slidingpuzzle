import sys
import numpy as np
import heapq


def solve(puzzle2D):  # accepts m x n puzzles
    nppuzzle2D = np.array(puzzle2D)
    numRows = nppuzzle2D.shape[0]
    numCols = nppuzzle2D.shape[1]
    numRowsAway = -1
    for index, token in np.ndenumerate(puzzle2D):
        if (token == 0):
            numRowsAway = numRows-(index[0]+1)  # 0-indexing not helpful here

    nppuzzle1D = nppuzzle2D.flatten()
    nppuzzle1D = np.delete(nppuzzle1D, np.where(nppuzzle1D == 0))
    inversions = numInversions(nppuzzle1D)

    if (numCols % 2 == 1 and inversions % 2 == 0):
        return getMinLenSoln(nppuzzle1D, numCols, numRows)
    elif (numCols % 2 == 0):
        if ((inversions + numRowsAway) % 2 == 0):
            return getMinLenSoln(nppuzzle1D, numCols, numRows)
    else:
        return None


def numInversions(puzzle1D):  # how many elements after a given one are less than it
    inversions = 0
    print(puzzle1D)
    for ptr in range(len(puzzle1D)):
        for cmp in range(ptr+1, len(puzzle1D)):
            if (puzzle1D[ptr] > puzzle1D[cmp]):
                inversions += 1
    return inversions


def getMinLenSoln(puzzle1D, width, height):
    solution = ['L', 'L', 'L', 'U']
    return solution


class State:  # current puzzle layout
    def __init__(self):
        #
        print("init of state class")

    # The heapq module will also be useful, as it provides functions to alter a list as if it were a priority queue.
    def __hash__(self) -> int:
        pass


# State class will be inside of a closed list --> need to be hashable for efficiency.
# This means that you will need to make sure that your State object includes a “magic” hash () method.
# The heapq module will also be useful, as it provides functions to alter a list as if it were a
# priority queue.

"""
FUN ARTICLES


https://stackoverflow.com/questions/171512/how-would-i-implement-a-bit-map

15-puzzle being NP-Hard
https://www.wisdom.weizmann.ac.il/~oded/COL/puzzle.pdf

3-cycle permutations of the 15-puzzle
https://www.whitman.edu/Documents/Academics/Mathematics/2017/Howe.pdf

96-page research paper
https://pure.tue.nl/ws/portalfiles/portal/174692011/Final_BEP_Report_Tim_HouthuijsV1.0_06_07_2020.pdf
"""

"""
Extra credit:
There are better heuristics, that provide a better estimation of distance to
goal, that are still admissible. This will allow your solver to solve more complicated and
larger puzzles. Find one of these heuristics online, and implement it.
"""
