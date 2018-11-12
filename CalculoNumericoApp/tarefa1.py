import math
import norma
import util
import parametros
import construtor
import sigma
import gauss
import jacobi
import numpy as np

n = 30
x = np.zeros(n)
t = np.zeros(n)
y = np.zeros(n)
h = np.zeros(n)
u = np.zeros(n)
l = np.zeros(n)
d = np.zeros(n)
Matriz = np.zeros((n,n))

def inicializar():
    global x
    x = [0, 1, 2.4, 4.1, 6.0, 8.2, 10.6, 13.4, 16.4, 19.7, 
         23.3, 27.0, 31.2, 35.5, 40.1, 45.0, 50.2, 55.6, 61.3, 67.3, 
         73.6, 80.1, 86.9, 94.0, 101.3, 109.0, 116.9, 125.0, 133.4, 142.1]

    global t
    for i in range(0, n, 1):
        t[i] = (i / 60)

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

def exercicio1():
    print("Exercicio 1")
    inicializar()
    sigma_0 = sigma.sigma(Matriz,n)
    if sigma_0 < 1:
        print("Estritamente Diagonal!\n")
    else:
        print("Não é estitamente Diagonal!\n")
    print("Sigma: {:.30f}\n".format(sigma_0))

def exercicio2():
    print("Exercicio 2")
    inicializar()
    tol = 10 ** -8
    k = util.estimarIteracao(n,Matriz,d,tol)

    print("Valor estimado de N: " + str(k) + "\n")

def exercicio3():
    print("Exercicio 3")
    tol = 10 ** -8
    inicializar()
    k = util.estimarIteracao(n,Matriz,d,tol)
    inicializar()
    y_gauss = gauss.gauss(n,Matriz,d)
    inicializar()
    y_jacobi = jacobi.jacobi(n,Matriz,d,tol,k)

    print("Distância entre y(N) e y* com N=" + str(k) + ": " + str(norma.norma(y_gauss,y_jacobi,n)) + "\n")

def exercicio4_5():
    print("Exercicios 4 e 5")
    inicializar()
    M = gauss.gauss(n,Matriz,d)
    A = parametros.parametroA(x,M,h,n)
    B = parametros.parametroB(x,M,h,n)

    print("Sistema resolvido pelo método de Gauss: \n")

    print("M: ")
    for i in range(n):
        print(str(M[i]))
    print("A: ")
    for i in range(n):
        print(str(A[i]))
    print("B: ")
    for i in range(n):
        print(str(B[i]))
    print("\n")
    
    inicializar()
    M = jacobi.jacobi_iter(n,Matriz,d,40)
    A = parametros.parametroA(x,M,h,n)
    B = parametros.parametroB(x,M,h,n)

    print("Sistema resolvido pelo método de Jacobi: \n")

    print("M: ")
    for i in range(n):
        print(str(M[i]))
    print("A: ")
    for i in range(n):
        print(str(A[i]))
    print("B: ")
    for i in range(n):
        print(str(B[i]))
    print("\n")

def main():
    exercicio1()
    exercicio2()
    exercicio3()
    exercicio4_5()

if __name__ == "__main__":
    main()