import math
import norma
import util
import parametros
import construtor
import sigma
import gauss
import jacobi
import numpy as np

#emax_xeq = np.zeros(101)
#emax_xchev = np.zeros(101)
emax_xeq_n = np.zeros(101)
emax_xchev_n = np.zeros(101)

def inicializar():
    #global emax_xeq
    #global emax_xchev
    global emax_xeq_n
    global emax_xchev_n

    for i in range(2,50):
        temp = util.erroMaxNewton(i)
        #emax_xeq[i] = temp[0]
        #emax_xchev[i] = temp[1]
        emax_xeq_n[i] = temp[0]
        emax_xchev_n[i] = temp[1]

        print("n = " + str(i) + "\nEmax_Xeq_Newton = " + str(emax_xeq_n[i]) + "\nEmax_Xchev_Newton = " + str(emax_xchev_n[i]) + "\n")
        #print("Emax_Xeq = " + str(emax_xeq[i]) + "\nEmax_Xchev = " + str(emax_xchev[i]) + "\n")

def ex1():
    inicializar()

    #print("\nCalculando os valores de log(Emax_Xeq) Newton: ")
    #for i in range(2,101):
    #    print(str(math.log10(emax_xeq[i])))
        
    #print("\nCalculando os valores de log(Emax_Xeq) Lagrange: ")
    #for i in range(2,101):
    #    print(str(math.log10(emax_xeq[i])))

    print("\nCalculando os valores de log(Emax_Xchev) Lagrange: ")
    for i in range(2,101):
        print(str(math.log10(emax_xchev_n[i])))
    
    print("\nCalculando os valores de log(Emax_Xchev) Newton: ")
    for i in range(2,101):
        print(str(math.log10(emax_xchev_n[i])))

def main():
    ex1()

if __name__ == "__main__":
    main()