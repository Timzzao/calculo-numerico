import math
import numpy as np

def sigma(A,n):
    vetorSigma = np.zeros(n)
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if not (i == j):
                vetorSigma[i] += A[i][j]
        vetorSigma[i] /= A[i][i]
    return vetorSigma.max()
