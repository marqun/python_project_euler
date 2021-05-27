"""A palindromic number reads the same both ways.
the largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""
import random
import time
start_time = time.time()
x= random.sample(range(1, 45), 5)
k=[]
for i in range(100,1000):
    for j in range(100,1000):
        n = i*j
        digits = [int(x) for x in str(n)]
        if len(digits)>5:
            if digits[0] == digits[5] and digits[1] == digits [4] and digits[2] == digits[3]:
                k.append(n)

print(max(k))
y = (time.time() - start_time)
print("--- %s seconds ---" %y)