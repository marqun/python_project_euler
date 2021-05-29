import random
import time
start_time = time.time()
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
def prime(x):
    sol = False
    while sol == False:
        for i in range(2,x+1):
            if x%i == 0:
                #print(x, "is not prime number")
                sol = True
                break
            elif i==x-1:
                #print(x , "is prime number")
                sol = True
                return x
l=0
x=3
y=[2]
number = 4
while l<number:
    k=prime(x)
    if k != None:
        print("k", k)
        y.append(k)
        print("y", y)
        l = len(y)
        print("l", l)
    x += 2
print(number, ": " , y[number-1])

y = (time.time() - start_time)
print("--- %s seconds ---" %y)