import math
import norma
import util
import parametros
import construtor
import sigma
import gauss
import jacobi
import numpy as np

n = 10
x = np.zeros(n+1)
t = np.zeros(n+1)
y = np.zeros(n+1)
h = np.zeros(n+1)
u = np.zeros(n+1)
l = np.zeros(n+1)
d = np.zeros(n+1)
Matriz = np.zeros((n+1,n+1))

def inicializar(): 
    global x
    x = [2.00, 1.81, 1.64, 1.49, 1.36, 1.25, 1.16, 1.09, 1.04, 1.01, 1.00]

    global t
    for i in range(0, n+1, 1):
        t.append(i / 10.0)

    global h
    h = parametros.parametroH(t,n)
    global u
    u = parametros.parametroMi(h,n)
    global l
    l = parametros.parametroL(h,n)
    global d
    d = parametros.parametroD(x,h,t,n)
    global Matriz
    Matriz = construtor.construirMatriz(u,l,n)

def main():
    inicializar()
    M = gauss.gauss(n+1,Matriz,d)
    A = parametros.parametroA(x,M,h,n)
    B = parametros.parametroB(x,M,h,n)

    print("Sistema resolvido pelo método de Gauss: \n")

    for i in range(n+1):
        print("M[" + str(i) + "]: " + str(M[i]) + "\n")
    for i in range(n):
        print("A[" + str(i) + "]: " + str(A[i]) + "\n")
    for i in range(n):
        print("B[" + str(i) + "]: " + str(B[i]) + "\n")
    print("\n")
    
    inicializar()
    M = jacobi.jacobi(n,Matriz,d,0.00000000000001,40)
    A = parametros.parametroA(x,M,h,n)
    B = parametros.parametroB(x,M,h,n)

    print("Sistema resolvido pelo método de Jacobi: \n")

    for i in range(n+1):
        print("M[" + str(i) + "]: " + str(M[i]) + "\n")
    for i in range(n):
        print("A[" + str(i) + "]: " + str(A[i]) + "\n")
    for i in range(n):
        print("B[" + str(i) + "]: " + str(B[i]) + "\n")
    print("\n")

if __name__ == "__main__":
    main()
