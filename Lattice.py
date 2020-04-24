"""
Problem #15:

Starting in the top left of a 2 x 2 grid,
and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are in a 20 X 20 grid?

"""
import time
start_time = time.time()

def move(x, y, list, range):

    if(x == range and y == range):
        list.append(1)
        print(list.__len__())
    if(x > range or y > range):
        return;

    move(x, y+1, list, range)
    move(x+1, y, list, range)

list = []
range = 20
move(0, 0, list, range)
print("Paths: " + str(list.__len__()))
print("--- %s seconds ---" % (time.time()-start_time))

