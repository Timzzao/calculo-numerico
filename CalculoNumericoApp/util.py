import math
import sigma
import norma
import runge
import lagrange
import numpy as np

malha = 10117

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
        print("Epsilon na iteração " + str(k) + ": " + str(eps))
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

def somaProdFuncoes(Fa, Fb, n):
    soma = 0

    for i in range(n):
        soma += (Fa[i] * Fb[i])

    return soma

def diferencasDivididas(Y, X, k):
    M = np.zeros((k, k));

    for i in range(k):
        M[i][0] = Y[i]

    for j in range(1, k, 1):
        for i in range(k-j):
            M[i][j] = 1.0/(X[i+j] - X[i]) * (M[i+1][j-1] - M[i][j-1])

    return M[0]

def newton(x, Y, X, k):
    M = diferencasDivididas(Y, X, k)

    #N = np.zeros(k)

    #for i in range(k):
    #    N[i] = M[0][i]

    sum = 0
    prod = 1

    for i in range(k):
        prod = M[i]

        for j in range(i):
            prod *= x-X[j]

        sum += prod

    return sum

def Tn(a, b, n):
    h = (b-a)/n
    sum = 0.0

    sum += np.exp(a)

    for i in range(1, n):
        sum += 2.0 * np.exp(a+h*i)

    sum += np.exp(b)

    return h/2.0*sum

def Sn(a, b, n):
    h = (b-a)/n
    sum = 0.0

    sum += np.exp(a)

    for i in range(1, n):
        sum += 2 * 2**(i%2) * np.exp(a+h*i)

    sum += np.exp(b)

    return h/3.0*sum

def erroMaxRunge(m):
    n = m+1

    x_eq = []
    x_chev = []
    x_malha = []

    f_eq = []
    f_chev = []
    f_malha = []

    pn_eq = []
    pn_chev = []

    for i in range(n):
        x_eq.append(-1.0 + 2.0*i/m)
        x_chev.append(-math.cos(i*math.pi/m))
        f_eq.append(runge.runge(x_eq[i]))
        f_chev.append(runge.runge(x_chev[i]))

    for i in range(malha+1):
        x_malha.append(-1.0 + 2.0*i/malha)
        f_malha.append(runge.runge(x_malha[i]))
        pn_eq.append(lagrange.interpolador(x_eq, f_eq, x_malha[i], n))
        pn_chev.append(lagrange.interpolador(x_chev, f_chev, x_malha[i], n))

    emax_xeq = norma.norma(pn_eq, f_malha, malha+1)
    emax_xchev = norma.norma(pn_chev, f_malha, malha+1)

    return [emax_xeq, emax_xchev]

def erroMaxSin(m):
    n = m+1

    x_eq = []
    x_chev = []
    x_malha = []

    f_eq = []
    f_chev = []
    f_malha = []

    pn_eq = []
    pn_chev = []

    for i in range(n):
        x_eq.append(-1.0 + 2.0*i/m)
        x_chev.append(-math.cos(i*math.pi/m))
        f_eq.append(math.sin(x_eq[i]))
        f_chev.append(math.sin(x_chev[i]))

    for i in range(malha+1):
        x_malha.append(-1.0 + 2.0*i/malha)
        f_malha.append(math.sin(x_malha[i]))
        pn_eq.append(lagrange.interpolador(x_eq, f_eq, x_malha[i], n))
        pn_chev.append(lagrange.interpolador(x_chev, f_chev, x_malha[i], n))

    emax_xeq = norma.norma(pn_eq, f_malha, malha+1)
    emax_xchev = norma.norma(pn_chev, f_malha, malha+1)

    return [emax_xeq, emax_xchev]

def erroMaxNewton(m):
    n = m+1

    x_eq = []
    x_chev = []
    x_malha = []

    f_eq = []
    f_chev = []
    f_malha = []

    p_lagrange_eq = []
    p_lagrange_chev = []
    p_newton_eq = []
    p_newton_chev = []

    for i in range(n):
        x_eq.append(-1.0 + 2.0*i/m)
        x_chev.append(-(math.cos(i*math.pi/m)))
        f_eq.append(math.sin(x_eq[i]))
        f_chev.append(math.sin(x_chev[i]))

    for i in range(malha+1):
        x_malha.append(-1.0 + 2.0*i/malha)
        f_malha.append(math.sin(x_malha[i]))
        #p_lagrange_eq.append(lagrange.interpolador(x_eq, f_eq, x_malha[i], n))
        #p_lagrange_chev.append(lagrange.interpolador(x_chev, f_chev, x_malha[i], n))
        p_newton_eq.append(newton(x_malha[i], f_eq, x_eq, n))
        p_newton_chev.append(newton(x_malha[i], f_chev, x_chev, n))

    #emax_xeq = norma.norma(f_malha, p_lagrange_eq, malha)
    #emax_xchev = norma.norma(f_malha, p_lagrange_chev, malha)

    emax_newton_eq = norma.norma(p_newton_eq, f_malha, malha)
    emax_newton_chev = norma.norma(p_newton_chev, f_malha, malha)

    return [emax_newton_eq, emax_newton_chev]