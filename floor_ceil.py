import numpy as np
np.set_printoptions(legacy='1.13')
val = np.array([float(i) for i in input().split()])
print(np.floor(val))
print(np.ceil(val))
print(np.rint(val))
