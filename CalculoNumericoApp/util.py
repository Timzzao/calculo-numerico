import math
import sigma
import norma
import numpy as np

def estimarIteracao(m,A,y,tol):
    eps = tol+1
    y_0 = np.zeros(m)
    y_1 = np.zeros(m)

    for k in range(0, m, 1):
        y_1[k] = y[k] / A[k][k]

    sigma_0 = sigma.sigma(A, m)
    norma_0 = norma.norma(y_1,y_0,m)

    k=0

    while(eps > tol):
        eps = (sigma_0 ** k)/(1-sigma_0)*norma_0
        k += 1
    return k

def buscaBinaria(t,T,n):
    M = n
    m = 0
    if (t > T[n-1]) or (t < T[0]):
        print("Valor fora do intervalo\n")
        return 0
    while abs(M - m) > 1:
        k = (M+m)//2
        if(t > T[k]):
            m = k
        else:
            M = k
    return m

def splineCubico(t,M,h,A,B,T,n):
    i = buscaBinaria(t,T,n)
    tal = 12 #numero do nosso grupo

    valor = M[i]/(6.0 * h[i+1]) * ((T[i+1] - t) ** 3)
    valor += M[i+1]/(6.0 * h[i+1]) * ((t - T[i]) ** 3)
    valor += A[i] * (t - T[i]) + B[i]
    valor -= (100 - 2*tal)

    return valor

def derivadaSC(t,M,h,A,B,T,n):
    i = buscaBinaria(t,T,n)

    valor = -M[i]/(2 * h[i+1]) * ((T[i+1] - t) ** 2)
    valor += M[i+1]/(2 * h[i+1]) * ((t - T[i]) ** 2)
    valor += A[i]

    return valor

def segundaDerivadaSC(t,M,h,A,B,T,n):
    i = buscaBinaria(t,T,n)

    valor = M[i]/h[i+1] * (T[i+1] - t)
    valor += M[i+1]/h[i+1] * (t - T[i])

    return valor