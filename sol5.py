"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
value = False
j=20
while value==False:
    for i in range(11,21):
        if j%i==0:
            if i==20:
                print("number:", j)
                value=True
        else:
            j+=20
            break
