import math
import util

def newton(w,M,h,A,B,T,n,tol):
    y_old = w
    k = 0

    print("y[" + str(k) + "]: " + str(y_old) + "\n")

    sup = inf = 0

    while sup*inf >= 0:
        k += 1
        fy = util.splineCubico(y_old,M,h,A,B,T,n)
        dy = util.derivadaSC(y_old,M,h,A,B,T,n)
        y_new = y_old - (fy/dy)

        print("y[" + str(k) + "]: " + str(y_new) + "\n")

        sup = util.splineCubico((y_new + tol),M,h,A,B,T,n)
        inf = util.splineCubico((y_new - tol),M,h,A,B,T,n)

        y_old = y_new
    return y_new

def newton_with_Max(w,M,h,A,B,T,n,Max):
    y_old = w
    k = 0

    print("y[" + str(k) + "]: " + str(y_old) + "\n")

    while k <= Max:
        k += 1
        fy = util.splineCubico(y_old,M,h,A,B,T,n)
        dy = util.derivadaSC(y_old,M,h,A,B,T,n)
        y_new = y_old - (fy/dy)

        print("y[" + str(k) + "]: " + str(y_new) + "\n")
        y_old = y_new
    return y_new