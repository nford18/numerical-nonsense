#################################################
#    Numerical Approximations for Integration   #
#################################################

def simpRule(lBound, rBound, step, func):
    a = lBound
    b = rBound
    dx = step
    N = int((b-a)/dx)
    sum = func(a) + func(b) # edge cases
    for i in range(1, N, 2): # odd cases
        sum += 4*func(a + i*dx)
    for i in range(2, N, 2): # even cases
        sum += 2*func(a + i*dx)
    sum *= dx/3 
    return sum


####################################
#           Riemann Sums           #
####################################
def LRAM(lBound, rBound, step, func):
    # constants:
    a = lBound
    b = rBound
    dx = step
    N = int((b-a)/dx)
    sum = 0
    for i in range(0,N-1):
        sum += func(a + i*dx)*dx
    return sum

def RRAM(lBound, rBound, step, func):
    # constants:
    a = lBound
    b = rBound
    dx = step
    N = int((b-a)/dx)
    sum = 0
    for i in range(1,N):
        sum += func(a + i*dx)*dx
    return sum

def MRAM(lBound, rBound, step, func):
    # constants:
    a = lBound
    b = rBound
    dx = step
    N = int((b-a)/dx)
    sum = 0
    for i in range(0,N-1):
        sum += dx*func(a + i*dx + dx/2)
    return sum

def TRAM(lBound, rBound, step, func):
    # constants:
    a = lBound
    b = rBound
    dx = step
    N = int((b-a)/dx)
    sum = 1/2 * (func(a) + func(b))
    for i in range(1,N):
        sum += func(a + i*dx)/2
    sum *= dx
    return sum