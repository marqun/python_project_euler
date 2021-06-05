"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""

y = 2**1000
y = str(y)
z=0
for i in y:
    z = z + int(i)

print(z)