import math
import norma
import util
import parametros
import construtor
import sigma
import gauss
import jacobi
import numpy as np

emax_xeq = np.zeros(51)
emax_xchev = np.zeros(51)

def inicializar():
    global emax_xeq
    global emax_xchev

    for i in range(2,51):
        temp = util.erroMaxSin(i)
        emax_xeq[i] = temp[0]
        emax_xchev[i] = temp[1]

        print("n = " + str(i) + "\nEmax_Xeq = " + str(emax_xeq[i]) + "\nEmax_Xchev = " + str(emax_xchev[i]) + "\n")

def ex1():
    inicializar()

    print("\nCalculando os valores de log(Emax_Xeq): ")
    for i in range(2,51):
        print(str(math.log10(emax_xeq[i])))

    print("\nCalculando os valores de log(Emax_Xchev): ")
    for i in range(2,51):
        print(str(math.log10(emax_xchev[i])))

def main():
    ex1()

if __name__ == "__main__":
    main()

