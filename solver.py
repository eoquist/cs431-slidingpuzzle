import sys
import heapq

# The .puz files it accepts are text files of m × n puzzles, containing the proper numbers separated by spaces.
# The gap in the puzzle is represented by the . character.


def __init__(self):  # add extra params if need be
    print("Address of self = ", id(self))


def solve(self, puzzle2D):
    width = getWidth(puzzle2D)
    height = 0
    rowOfGap = 0
    for line in puzzle2D:
        height += 1
        for elem in line.split():
            if (elem == 0):
                rowOfGap = height
    puzzle1D = flatten(puzzle2D)
    inversions = numInversions(puzzle1D)

    if (width % 2 == 1 and inversions % 2 == 0):  # possible
        print("solvable")
        # need self when calling methods !!! ???
        return getMinLenSoln(puzzle1D, width, height)
    elif (width % 2 == 0):
        if ((inversions + (height - rowOfGap)) % 2 == 0):
            print("solvable")
            return getMinLenSoln(puzzle1D, width, height)
    else:
        return None


def getMinLenSoln(self, puzzle1D, width, height):
    print("oof")

# logn searching through states
# PQ states? Unsure
# Python standard PQ class stand-in
# Opt. python imaging library
# → closed list :) needed bc not tree & hash tables review ===> stack LIFO path
# Python magic methods -- first arg should be self
# Using dicts/simple tables?
# The Manhattan distance between two points x = (x 1, x 2, …, x n ) and y = (y 1, y 2, …, y n ) in n-dimensional space is the sum of the distances in each dimension
# Manhattan distance is calculated as the sum of the absolute differences between the two vectors.


def getWidth(self, puzzle2D):
    width = 0
    for elem in puzzle2D[0].split():
        width += 1
    return width


def flatten(self, puzzle2D):  # I might need to keep track of the dimensions n x m
    puzzle1D = [row.split() for row in puzzle2D]
    return puzzle1D


def numInversions(self, puzzle1D):  # how many elements after a given one are less than it
    inversions = 0
    for ptr in range(len(puzzle1D)):
        for cmp in range(i+1, len(puzzle1D)):
            if (ptr > cmp):
                inversions += 1
    print("num inversions " + inversions)
    return inversions


class State:
    def __init__(self):
        #
        print("init of state class")

    # The heapq module will also be useful, as it provides functions to alter a list as if it were a priority queue.
    def __hash__(self) -> int:
        pass


if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")


# A* state class which designates a state of the puzzle (that is, a current layout of all the tiles).

# State class will be inside of a closed list --> need to be hashable for efficiency.
# This means that you will need to make sure that your State object includes a “magic” hash () method.
# The heapq module will also be useful, as it provides functions to alter a list as if it were a
# priority queue.


print("notes below")
# The gap will be represented by a 0. It will return one of two things:
#  If the puzzle is not solvable, it will return None.
#  If the puzzle is solvable, it will return a solution of minimum length.

# note to self
# think of other ways to visualize the sliding puzzle


# Extra credit:
# There are better heuristics, that provide a better estimation of distance to
# goal, that are still admissible. This will allow your solver to solve more complicated and
# larger puzzles. Find one of these heuristics online, and implement it.
