

import numpy as np
n, m =  map(int, input().split())
val = np.array([[int(i) for i in input().split()] for j in range(n)])
print(val.transpose())
print(val.flatten())
