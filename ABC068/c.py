import numpy as np

N, M = map(int, input().split())
ab = np.empty((0,2), int)
for i in range(M):
    a, b = map(int, input().split())
    ab = np.append(ab, np.array([[a,b]]), axis=0)
print("POSSIBLE")