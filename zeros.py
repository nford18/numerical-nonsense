#################################################
#   Numerical Approximations for Finding Zeros  #
#################################################

def newtons(guess, tolerance, func, deriv):
    x0 = float(guess)
    tol = tolerance
    dx = 10*tol
    while(dx>tol):
        x1 = x0 -func(x0)/deriv(x0)
        dx = abs(x1 - x0)
        x0 = x1
    return x0

def bisection(lBound, rBound, tolerance, func):
    a = lBound
    b = rBound
    tol = tolerance
    dx = abs(b-a)
    while(dx>tol):
        midpoint = (a+b)/2
        if(func(midpoint) == 0):
            dx = tol
        elif(func(a)*func(midpoint) < 0):
            b = midpoint
        else:
            a = midpoint
        dx = abs(b-a)
    return (a+b)/2