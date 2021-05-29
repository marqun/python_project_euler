"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

import time
start_time = time.time()

a=1
b=1
c=1

for i in range (1,1000):
    for j in range(1, 1001-i):
        for k in range(1,1001-i-j):
            if i+j+k ==1000 and i*i+j*j==k*k:
                print("this is it!",i, j ,k)
                break


y = (time.time() - start_time)
print("--- %s seconds ---" %y)