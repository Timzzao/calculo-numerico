import math
import util

def newton(w,M,h,A,B,T,n,tol,Max):
    y_old = w
    k = 0

    print("y[" + str(k) + "]: " + str(y_old) + "\n")

    sup = inf = 0

    k = 0

    while sup*inf >= 0 and k <= Max:
        k += 1
        fy = util.splineCubico(y_old,M,h,A,B,T,n)
        dy = util.derivadaSC(y_old,M,h,A,B,T,n)
        y_new = y_old - (fy/dy)

        print("y[" + str(k) + "]: " + str(y_new) + "\n")

        sup = util.splineCubico((y_new + tol),M,h,A,B,T,n)
        inf = util.splineCubico((y_new - tol),M,h,A,B,T,n)

        y_old = y_new
    return y_new