import numpy as np

a = np.array([
    [1, -1, 2, 4, 0],
    [8, 2, 0, 5, 3],
    [0, 1, 2, 1, 2]
])

b = np.array([
    [1,0,1,0],
    [0,0,2,-1],
    [1,0,1,1],
    [0,1,1,1],
    [1,1,0,-1]
])

print(np.dot(a, b))
print(a)