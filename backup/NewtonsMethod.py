# imports
import math

def f(x):
    y = math.exp(x) - 1.2*x - 2*x**2
    # y=x*math.exp(x) -1
    return y
def df(x):
    y = math.exp(x) - 1.2 - 4*x
    # y=x*math.exp(x) + math.exp(x)
    return y

a = 0
b = 3
x0 = 0.0
tol = 10**(-5)
dx = 10*tol

i=0
print("dx:", dx)
print("tol", tol)
while(dx>tol):
    print("iter", i, ":", dx, sep = ' ')
    x1 = x0 -f(x0)/df(x0)
    dx = abs(x1 - x0)
    x0 = x1
    i+=1


print('Zero found at x = ', x0,' in ', i,' interations')