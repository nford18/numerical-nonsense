def f(x):
    return 1


def trapApprox():
    # constants:
    a = 0
    b = 10
    N = 100
    dx = (b-a)/N

    sum = 1/2 * (f(a) + f(b))
    for k in range(1,N):
        x = a + k*dx
        sum += f(x)/2
        
    Int = sum*dx