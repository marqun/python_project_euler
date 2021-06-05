"""The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million."""
lmax = 1
jmax = 1
for j in range(1, 100):
    l = 1
    k=j
    print("\nj:", j)
    while j != 1:
        if j % 2 == 0:
            j=j/2
            print("j:", j)
            l += 1
        elif j % 2 != 0:
            j=3*j+1
            print("j:", j)
            l+= 1
        if j == 1: print("l:", l, "lmax:", lmax)
        if l>lmax :
            lmax = l
            jmax = k
print("k:", k, "lmax:", lmax)
