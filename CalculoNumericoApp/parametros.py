import math
import numpy as np

def parametroH(t,n):
    h = np.zeros(n)
    for i in range(0, n - 1, 1):
        h[i+1] = t[i+1] - t[i]
    return h

def parametroMi(h,n):
    u = np.zeros(n)
    for i in range(0, n - 1, 1):
        u[i] = h[i] / (h[i] + h[i+1])
    return u

def parametroL(h,n):
    l = np.zeros(n)
    for i in range(1, n - 1, 1):
        l[i] = h[i+1] / (h[i] + h[i+1])
    return l

def parametroD(x,h,t,n):
    d = np.zeros(n)
    d[0] = 2 * ((x[2] - x[1])/(t[2] - t[1]) - (x[1] - x[0])/(t[1] - t[0]))/(t[2] - t[0])
    d[n-1] = 2 * ((x[n-1] - x[n-2])/(t[n-1] - t[n-2]) - (x[n-2] - x[n-3])/(t[n-2] - t[n-3]))/(t[n-1] - t[n-3])

    for i in range(1, n - 1, 1):
        d[i] = (6.0 / (h[i] + h[i+1])) * ((x[i+1] - x[i])/h[i+1] - (x[i] - x[i-1])/h[i])
    return d

def parametroB(y,M,h,n):
    B = np.zeros(n)
    for i in range (0, n - 1, 1):
        B[i] = y[i] - (M[i] / 6.0) * pow(h[i+1], 2)
    return B

def parametroA(y,M,h,n):
    A = np.zeros(n)
    for i in range (0, n - 1, 1):
        A[i] = (((y[i+1] - y[i]) / h[i+1]) - (((M[i+1] - M[i]) / 6.0) * h[i+1]))
    return A
