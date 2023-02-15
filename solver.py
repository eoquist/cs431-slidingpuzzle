import sys
import numpy as np
import heapq as hq
from queue import PriorityQueue
import math


def solve(puzzle2D):  # accepts m x n puzzles
    nppuzzle_2D = np.array(puzzle2D)
    numRows = nppuzzle_2D.shape[0]
    numCols = nppuzzle_2D.shape[1]
    numRowsAway = -1
    for index, token in np.ndenumerate(puzzle2D):
        if (token == 0):
            numRowsAway = numRows-(index[0]+1)  # 0-indexing not helpful here

    nppuzzle_1D = nppuzzle_2D.flatten()
    nppuzzle_1D = np.delete(nppuzzle_1D, np.where(nppuzzle_1D == 0))
    inversions = get_num_inversions(nppuzzle_1D)
    nppuzzle_1D = nppuzzle_2D.flatten()  # re-include the gap

    if (numCols % 2 == 1 and inversions % 2 == 0):
        return get_minlen_soln(nppuzzle_2D)
    elif (numCols % 2 == 0):
        if ((inversions + numRowsAway) % 2 == 0):
            return get_minlen_soln(nppuzzle_2D)
    else:
        return None


# how many elements after a given one are less than it
def get_num_inversions(puzzle_1D):
    inversions = 0
    print(puzzle_1D)
    for ptr in range(len(puzzle_1D)):
        for cmp in range(ptr+1, len(puzzle_1D)):
            if (puzzle_1D[ptr] > puzzle_1D[cmp]):
                inversions += 1
    return inversions


"""
# easy.puz ['L', 'L', 'L', 'U']
"""


def get_minlen_soln(nppuzzle_2D):
    solution = np.array([])
    open_list = PriorityQueue()
    closed_list = dict()  # https://www.w3schools.com/python/python_ref_dictionary.asp
    start_state = State(nppuzzle_2D, 0)

    open_list.put(start_state)
    while (True):
        current_state = open_list.get()
        current_puzzle = current_state.puzzle
        if current_puzzle in closed_list:
            # dont do anything

            # closed is a dict where the key is a state and the value is the previous state
            # heapq module also useful - provides functions to alter a list like a pq.
            # hq.heapify(open_list)
            # hq.heappush(open_list, State(tup_puzzle))

            # state = hash(State(tup_puzzle))
            # child_states ?

    closed_list.update({start_state: start_state})  # temporary
    # closed is a dict where the key is a state and the value is the previous state

    char = 'L'
    solution = np.append(solution, char)

    return solution

# logn searching through states
# Opt. python imaging library

# An easy heuristic to use is to relax the problem so that tiles can move through each
# other, and count the number of moves that would be necessary. For example, in the given
# puzzle the 1 tile must move left once and up twice, for 3 moves. Adding this up for every
# tile, we find that this heuristic estimates this state to be 19 moves away from the goal state.


class State:
    # f(x) = g(x)+h(X) = next state cost + admissible heuristic cost (to goal)
    def __init__(self, puzzle, depth):
        self.puzzle = puzzle
        self.depth = depth
        self.cost = self.calculate_heuristic()
        self.is_solved = self.cost == 0
        self.cost += depth

    def __hash__(self):
        return hash(tuple(self.puzzle.flatten()))

    @classmethod
    def calculate_heuristic(self):
        cost = 0
        numRows = len(self.puzzle)
        numCols = len(self.puzzle[0])
        tup_puzzle = self.puzzle.flatten()
        for elem in tup_puzzle:
            if (elem != 0):
                index_1D = tup_puzzle.index(elem)
                # abs goal idx - curr idx
                vdist = math.floor(abs((elem-1) - index_1D) / numRows)
                hdist = (index_1D % numCols) - ((elem-1) % numCols)
                cost += (hdist + vdist)
        return cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > self.cost


"""
FUN ARTICLES


https://stackoverflow.com/questions/171512/how-would-i-implement-a-bit-map

Chess
https://www.chessprogramming.org/Hashing_Dictionaries

A GPU-Based Backtracking Algorithm for Permutation Combinatorial Problems
https://web.archive.org/web/20190220125411/http://pdfs.semanticscholar.org/23c1/80675762ded21c901dcd023aee8babaa85b5.pdf

15-puzzle being NP-Hard
https://www.wisdom.weizmann.ac.il/~oded/COL/puzzle.pdf

3-cycle permutations of the 15-puzzle
https://www.whitman.edu/Documents/Academics/Mathematics/2017/Howe.pdf

96-page research paper
https://pure.tue.nl/ws/portalfiles/portal/174692011/Final_BEP_Report_Tim_HouthuijsV1.0_06_07_2020.pdf


============================

Extra credit:
There are better heuristics, that provide a better estimation of distance to
goal, that are still admissible. This will allow your solver to solve more complicated and
larger puzzles. Find one of these heuristics online, and implement it.
"""
