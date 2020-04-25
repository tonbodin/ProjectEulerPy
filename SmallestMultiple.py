"""

Problem #5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


"""
import time
start_time = time.time()
def test(n):
    for i in range(20, 1, -1):
        if(n % i != 0):
            return False
    return True

n = 2520
while test(n) is False:
    n += 20

print("Answer is: " + str(n))
print("--- %s seconds ---" % (time.time()-start_time))