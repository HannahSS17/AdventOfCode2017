import numpy as np

f = open("data.txt")
X = np.loadtxt(f)

res = []

# i - elements, j - row
for i in range(len(X)):
    for j in range(len(X[1])):
        for k in range(len(X[0])):
            cur_val = X[i][j]

            if i != len(X):
                next_val = X[i][k]
            else:
                next_val = X[i][0]

            if cur_val % next_val == 0 and (cur_val != next_val) and (cur_val > next_val):
                A = cur_val / next_val
                res.append(A)

print(sum(res))
