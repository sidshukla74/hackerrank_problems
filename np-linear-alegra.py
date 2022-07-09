#https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy as np
n = int(input())
val = np.array([[float(i) for i in input().split()] for j in range(n)])
print(round(np.linalg.det(val), 2))
