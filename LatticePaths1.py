"""
Problem #15:

Starting in the top left of a 2 x 2 grid,
and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are in a 20 X 20 grid?
"""
import time
start_time = time.time()

dim = 20
grid = [[1]*(dim + 1)]*(dim+1)

for i in range(dim - 1, -1, -1):
    for j in range(dim - 1, -1, -1):
        grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

print("Grid Dimensions: " + str(dim) + "x" + str(dim))
print("Paths: " + str(grid[0][0]))
print("--- %s seconds ---" % (time.time()-start_time))


"""
OUTPUT:
Grid Dimensions: 20x20
Paths: 137846528820
--- 0.0009987354278564453 seconds ---
"""


