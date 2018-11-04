import math
import numpy as np

def construirMatriz(u,l,n):
    Matriz = np.zeros((n, n))
    for i in range(0, n-1, 1):
        Matriz[i][i] = 2.0
        Matriz[i][i+1] = l[i]
        if i > 0:
            Matriz[i][i-1] = u[i]
    Matriz[n-1][n-1] = 2.0
    Matriz[n-1][n-2] = u[n-1]
    return Matriz