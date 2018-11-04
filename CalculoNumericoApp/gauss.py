import math
import construtor
import numpy as np

def gauss(m,A,y):
    for j in range(m):
        if A[j][j] == 0:
            k = j
            while True:
                if 0 == A[k][j]:
                    k += 1
                    if(k == m):
                        print("Matriz Inválida!\n")
                        break
                else:
                    temp = A[k].copy()
                    A[k] = A[j].copy()
                    A[j] = temp.copy()
                    break
        for i in range(j+1,m):
            mult = - A[i][j] / A[j][j]
            for k in range(j,m-1):
                A[i][k] += mult * A[j][k]
            y[i] += mult * y[j]
    x = np.zeros(m)
    for i in range(m-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1,m):
            x[i] -= (A[i][j] * x[j])
        x[i] = x[i] / A[i][i]
    return x