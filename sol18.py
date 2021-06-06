import numpy as np
g=15
x= """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

y = np.zeros((g, g))

l = 0
k = 0
while k < g:
    #print("\n-------------\nk:", k)
    for j in range(0, k+1):
        y[k][j] = int(x[l]+x[l+1])
        #print("k:", k , "j:", j, x[l], x[l+1])
        l += 3
    k += 1

max = np.zeros((g,g))
while g>0:
    for i in range(g-1,-1,-1):
        print(y[i])
        for j in range(g-1,-1,-1):
            if j>0:
                if y[i][j]+y[i][j-1]>y[i][j]+y[i-1][j-1]: max[i-1][j-1] = y[i][j]+y[i][j-1]
                else: max[i-1][j-1] = y[i][j]+y[i-1][j-1]
                print("max[i-1][j-1]:", max[i-1][j-1], [i-1], [j-1])
    g -= 1
    print(g)


print(max)