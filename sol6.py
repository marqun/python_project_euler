"""The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
x = 100
y = 0
z = 0
for i in range(1,x+1):
    y+= (i*i)
    #print("i:", i , "y:", y)
    z+=i
    if i == x:
        z= z*z
        #print("z:", z)

print("solution:", z-y)