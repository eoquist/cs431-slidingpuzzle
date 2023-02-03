# This file will have one public function, called solve().
# solve() will take one argument: a 2D row-major list containing a puzzle.
# The gap will be represented by a 0. It will return one of two things:
#  If the puzzle is not solvable, it will return None.
#  If the puzzle is solvable, it will return a solution of minimum length.


# Since you are using A*, you will probably also want to create a State class. Because you will
# be putting this State inside of a closed list, it will need to be hashable for efficiency.
# Your state object should include a “magic” __hash__() method.
# The heapq module will also be useful, as it provides functions to alter a list as if it were a
# priority queue


# Extra credit: There are better heuristics, that provide a better estimation of distance to
# goal, that are still admissible. This will allow your solver to solve more complicated and
# larger puzzles. Find one of these heuristics online, and implement it.
