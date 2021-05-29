import random
import time
start_time = time.time()
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

l=1
x=1
while l<=10001:
    y = is_prime(x)
    if y == True:
        #print("l:", l, "x:", x, "y:", y)
        l+=1
        x+=1
    else:
        x+=1

print("l:", l-1, "x:", x-1, "y:", y)

y = (time.time() - start_time)
print("--- %s seconds ---" %y)