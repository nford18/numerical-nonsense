# imports
import math

def f(x):
    y = math.exp(x) - 1.2*x - 2*x**2
    # y=x*math.exp(x) -1
    return y

a = 0
b = 10
tol = 10^(-4)
dx = abs(b-a)

i=0
while(dx>tol):
    i += 1
    mid = (a+b)/2
    if(f(mid) == 0):
        print("if 1")
        dx = tol
    elif(f(a)*f(mid) < 0):
        print("if 2")
        b = mid
    else:
        print("if 3")
        a = mid
    dx = abs(b-a)

print("Zero found at x = ", (a+b)/2, " in ", i, " interations")
