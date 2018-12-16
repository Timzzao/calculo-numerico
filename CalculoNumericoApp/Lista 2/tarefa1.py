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
f1 = np.zeros(n)
f2 = np.zeros(n)
f3 = np.zeros(n)

y = np.zeros(3)
Matriz = np.zeros((3,3))
alfa = np.zeros(3)

def inicializar():
    global x
    x = [0, 1, 2.4, 4.1, 6.0, 8.2, 10.6, 13.4, 16.4, 19.7, 
         23.3, 27.0, 31.2, 35.5, 40.1, 45.0, 50.2, 55.6, 61.3, 67.3, 
         73.6, 80.1, 86.9, 94.0, 101.3, 109.0, 116.9, 125.0, 133.4, 142.1]
    for i in range(n):
        x[i] /= 100
        round(x[i], 30)

    global t
    for i in range(0, n, 1):
        t[i] = (i / 60.0)
        round(t[i], 30)

    global f1
    for i in range(n):
        f1[i] = 1.0
        round(f1[i], 30)

    global f2
    for i in range(n):
        f2[i] = t[i]
        round(f2[i], 30)

    global f3
    for i in range(n):
        f3[i] = t[i]**2
        round(f3[i], 30)

    global Matriz
    Matriz[0][0] = util.somaProdFuncoes(f1,f1,n)
    Matriz[0][1] = util.somaProdFuncoes(f1,f2,n)
    Matriz[0][2] = util.somaProdFuncoes(f1,f3,n)
    Matriz[1][1] = util.somaProdFuncoes(f2,f2,n)
    Matriz[1][2] = util.somaProdFuncoes(f2,f3,n)
    Matriz[2][2] = util.somaProdFuncoes(f3,f3,n)

    Matriz[1][0] = Matriz[0][1]
    Matriz[2][0] = Matriz[0][2]
    Matriz[2][1] = Matriz[1][2]

    round(Matriz[0][0], 30)
    round(Matriz[0][1], 30)
    round(Matriz[0][2], 30)
    round(Matriz[1][0], 30)
    round(Matriz[1][1], 30)
    round(Matriz[1][2], 30)
    round(Matriz[2][0], 30)
    round(Matriz[2][1], 30)
    round(Matriz[2][2], 30)

def ex1():
    inicializar()
    print("Imprimindo matriz A:")

    for i in range(3):
        for j in range(3):
            print(str(Matriz[i][j]))
        print("")

    y[0] = util.somaProdFuncoes(f1,x,n)
    round(y[0], 30)
    y[1] = util.somaProdFuncoes(f2,x,n)
    round(y[1], 30)
    y[2] = util.somaProdFuncoes(f3,x,n)
    round(y[2], 30)

    print("Imprimindo vetor Y (yi = <fi,xi>)")
    for i in range(3):
        print("Y[" + str(i) + "]: " + str(y[i]) + "\n")

    alfa = gauss.gauss(3,Matriz,y)

    print("Imprimindo vetor x (xi=alfa_i)")
    for i in range(3):
        print("X[" + str(i) + "]: " + str(alfa[i]) + "\n")

    print("Resultado para o valor de g: " + str(2.0*alfa[2]) + " m/s²")

def main():
    ex1()

if __name__ == "__main__":
    main()