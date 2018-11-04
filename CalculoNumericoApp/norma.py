import math
import numpy as np

def norma(x,y,n):
    dist = np.zeros(n+1)
    for i in range(0, n, 1):
        dist[i] = abs(x[i] - y[i])
    return dist.max()
