import math
import norma
import numpy as np

def jacobi(n,A,y,tol,n_max):
    eps = tol + 1
    k = 0
    x_old = np.zeros(n)
    x_new = np.zeros(n)

    while(k < n_max):
        x_new[0] = (y[0] - A[0][1] * x_old[1])/2

        for i in range(1,n-1):
            x_new[i] = (y[i] - A[i][i-1] * x_old[i-1] - A[i][i+1] * x_old[i+1])/2
        x_new[n-1] = (y[n-1] - A[n-1][n-2] * x_old[n-2])/2
        eps = norma.norma(x_new,x_old,n)
        if(eps <= tol):
            break
        x_old = x_new.copy()
        k += 1
    return x_new

def jacobi_iter(n,A,y,n_max):
    eps = tol + 1
    k = 0
    x_old = np.zeros(n)
    x_new = np.zeros(n)

    while(k < n_max):
        x_new[0] = (y[0] - A[0][1] * x_old[1])/2

        for i in range(1,n-1):
            x_new[i] = (y[i] - A[i][i-1] * x_old[i-1] - A[i][i+1] * x_old[i+1])/2
        x_new[n-1] = (y[n-1] - A[n-1][n-2] * x_old[n-2])/2
        x_old = x_new.copy()
        k += 1
    return x_new