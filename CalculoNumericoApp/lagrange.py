import math
import numpy as np


def L(j, x, X, n):
    produtorio = 1.0

    for i in range(n):
        if i != j:
            produtorio = produtorio * (x - X[i])/(X[j] - X[i])

    return produtorio

def interpolador(X,f,x,n):
    somatorio = 0

    for j in range(n):
        somatorio += f[j] * L(j, x, X, n)

    return somatorio