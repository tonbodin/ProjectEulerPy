
"""
 Problem #13: Longest Collatz Sequence

 The following sequence is defined for the set of positive integers
 		n -> n/2 (n is even)
 		n -> 3*n + 1 (n is odd)

 For example, for 13: 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

 Which starting number, under 1 million, produces the Longest Collatz sequence?
"""

import time
start_time = time.time()
def _function(num):
    changing_num = num;
    times = 0;
    while changing_num != 1:
        if changing_num % 2 == 0:
            changing_num /= 2
        else:
            changing_num = (changing_num * 3) + 1
        times = times + 1
    return times
ans = 0;
max_times = -9999
for i in range(1, 1000000):
    tmp = _function(i)
    if tmp > max_times:
        ans = i
        max_times = tmp
end_time = time.time()
print("Number: " + str(ans) + " Max Times: " + str(max_times))
print("--- %s seconds ---" % (time.time()-start_time))
