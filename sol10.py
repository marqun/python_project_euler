"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

import time
start_time = time.time()

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
z=0
x=1
while x<1000000:
    y=is_prime(x)
    if y == True: z+=x
    x+=1

print(z)

y = (time.time() - start_time)
print("--- %s seconds ---" %y)