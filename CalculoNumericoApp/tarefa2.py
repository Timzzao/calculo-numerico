import math
import norma
import util
import parametros
import construtor
import sigma
import gauss
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
    print("Exercicios 1")
    inicializar()
    M = gauss.gauss(n,Matriz,d)
    A = parametros.parametroA(x,M,h,n)
    B = parametros.parametroB(x,M,h,n)

    valoresDeTeste = np.zeros(n);
    valoresDeTeste[0] = (t[1] + t[0]) / 2

    print("Teste do polinomio")
    for i in range(1, n, 1):
        valoresDeTeste[i] = valoresDeTeste[i - 1] + (1.0/60)
        print(str(valoresDeTeste[i]))

    print("Teste do polinomio")
    for i in range(0, n, 1):
        temp = util.splineCubico(valoresDeTeste[i],M,h,A,B,t,n)
        print(str(temp))

    print("Teste da primeira derivada")
    for i in range(0, n, 1):
        temp = util.derivadaSC(valoresDeTeste[i],M,h,A,B,t,n)
        print(str(temp))

    print("Teste da segunda derivada")
    for i in range(0, n, 1):
        temp = util.segundaDerivadaSC(valoresDeTeste[i],M,h,A,B,t,n)
        print(str(temp))

def main():
    exercicio1()

if __name__ == "__main__":
    main()
