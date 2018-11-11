import math
import norma
import util
import parametros
import construtor
import sigma
import gauss
import newton
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

def exercicio1_2():
    print("Exercicios 1")
    inicializar()
    M = gauss.gauss(n,Matriz,d)
    print("Parametro M")
    print(str(np.array(M)))
    A = parametros.parametroA(x,M,h,n)
    print("Parametro A")
    print(str(np.array(A)))
    B = parametros.parametroB(x,M,h,n)
    print("Parametro B")
    print(str(np.array(B)))

    valoresDeTeste = np.zeros(n);
    valoresDeTeste[0] = (t[1] + t[0]) / 2

    print("Valores de t")
    for i in range(1, n, 1):
        valoresDeTeste[i] = valoresDeTeste[i - 1] + (1.0/60)
    print(str(np.array(valoresDeTeste)))

    print("Teste do polinomio")
    spline = np.zeros(n)
    for i in range(0, n, 1):
        spline[i] = util.splineCubico(valoresDeTeste[i],M,h,A,B,t,n)
    print(str(np.array(spline)))

    print("Teste da primeira derivada")
    derivada1 = np.zeros(n)
    for i in range(0, n, 1):
        derivada1[i] = util.derivadaSC(valoresDeTeste[i],M,h,A,B,t,n)
    print(str(np.array(derivada1)))

    print("Teste da segunda derivada")
    derivada2 = np.zeros(n)
    for i in range(0, n, 1):
        derivada2[i] = util.segundaDerivadaSC(valoresDeTeste[i],M,h,A,B,t,n)
    print(str(np.array(derivada2)))

    print("O intervalo escolhido é [t19, t20]")

    print("Exercicio 2")

    print("O chute será 0.33")

    raiz = newton.newton(0.33,M,h,A,B,t,n,10**-10,n)

    print("O t é: " + str(raiz))

def main():
    exercicio1_2()

if __name__ == "__main__":
    main()
