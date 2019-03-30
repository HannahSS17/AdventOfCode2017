import numpy as np

f = open("data.txt")

X = np.loadtxt(f)
max_per_col = X.max(axis=1)
min_per_col = X.min(axis=1)

a = np.subtract(max_per_col, min_per_col)
print(np.sum(a))
