import math
import norma
import util
import parametros
import construtor
import sigma
import gauss
import jacobi
import numpy as np

def pt1():
    print("Calculos dos valores exatods de ETn e ESn para n = 10, 20, ..., 100")

    for i in range(10, 101, 10):
        print("n = " + str(i))
        print("ETn = " + str(np.abs(np.exp(1) - np.exp(0) - util.Tn(0, 1, i))))
        print("ESn = " + str(np.abs(np.exp(1) - np.exp(0) - util.Sn(0, 1, i))))

def pt2():
    n = 10
    log_mi = np.zeros(n)
    log_hi = np.zeros(n)
    log_ETn = np.zeros(n)
    log_ESn = np.zeros(n)
    Y = np.zeros(2)
    X = np.zeros(2)
    M = np.zeros((2,2))

    print("Supondo uma aproximacao y=ax+b onde temos: ")
    print("y = log10(ETn) ou log10(ESn)")
    print("x = log10(h)")

    for i in range(n):
        log_mi[i] = 1.0

    print("log10(h)")
    for i in range(10, 101, 10):
        log_hi[int((i-10)/10)] = math.log10(1/i)
        print(str(log_hi[int((i-10)/10)]))
        
    print("log10(ETn)")
    for i in range(10, 101, 10):
        log_ETn[int((i-10)/10)] = math.log10(np.abs(np.exp(1) - np.exp(0) - util.Tn(0,1,i)))
        print(str(log_ETn[int((i-10)/10)]))
    
    print("log10(ETn)")
    for i in range(10, 101, 10):
        log_ESn[int((i-10)/10)] = math.log10(np.abs(np.exp(1) - np.exp(0) - util.Sn(0,1,i)))
        print(str(log_ESn[int((i-10)/10)]))

    print("Minimos quadrados")

    f1f1 = util.somaProdFuncoes(log_mi,log_mi,n)
    f1f2 = util.somaProdFuncoes(log_mi,log_hi,n)
    f2f2 = util.somaProdFuncoes(log_hi,log_hi,n)

    print("Coeficientes da Matriz:")
    print("<f1, f1> = " + str(f1f1))
    print("<f1, f2> = " + str(f1f2))
    print("<f1, f3> = " + str(f2f2))

    print("Coeficientes do vetor de entrada:")

    Y[0] = util.somaProdFuncoes(log_mi, log_ETn, n)
    Y[1] = util.somaProdFuncoes(log_hi, log_ETn, n)
    print("<f1, log(ETn)> = " + str(Y[0]))
    print("<f2, log(ETn)> = " + str(Y[1]))

    M[0][0] = f1f1
    M[0][1] = f1f2
    M[1][0] = f1f2
    M[1][1] = f2f2

    X = gauss.gauss(2,M,Y)

    print("Coeficientes para a reta log(ETn)")
    print("Angular: " + str(X[1]))
    print("Linear: " + str(X[0]))
    
    print("Coeficientes do vetor de entrada:")

    Y[0] = util.somaProdFuncoes(log_mi, log_ESn, n)
    Y[1] = util.somaProdFuncoes(log_hi, log_ESn, n)
    print("<f1, log(ESn)> = " + str(Y[0]))
    print("<f2, log(ESn)> = " + str(Y[1]))

    M[0][0] = f1f1
    M[0][1] = f1f2
    M[1][0] = f1f2
    M[1][1] = f2f2

    X = gauss.gauss(2,M,Y)

    print("Coeficientes para a reta log(ESn)")
    print("Angular: " + str(X[1]))
    print("Linear: " + str(X[0]))

def main():
    #pt1()
    pt2()

if __name__ == "__main__":
    main()


