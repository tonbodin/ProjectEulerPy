"""

Problem #23: Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import time
start_time = time.time()

def sumFactors(n):
    total = 0
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            total += i
    return total

list_fac = []
list_sums = [0]*28123

for i in range(1, 28123):
    if sumFactors(i) > i:
        list_fac.append(i)
print(list_fac.__len__())

for i in range(0, list_fac.__len__()):
    print(i)
    for j in range(i, list_fac.__len__()):
        tmp = list_fac[i] + list_fac[j]
        if(tmp < 28123):
            list_sums[tmp] = 1

total = 0
for i in range(0, list_sums.__len__()):
    if list_sums[i] != 1:
        total += i


print(total)
print("--- %s seconds ---" % (time.time()-start_time))
print("Done")

