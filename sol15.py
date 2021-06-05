"""Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"""

from math import factorial as f
print(f(40)/(f(20)*f(20)))