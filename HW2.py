import math

print("\nProblem 1:_______")
def integrand(x):
    return x*math.log(x)

a = 1
b = 2
N = 200
dx = (b-a)/N

sum_MRAM = 0
for i in range(0,N-1):
    sum_MRAM += dx*integrand(a + i*dx + dx/2)
print("Midpoint Riemann Sum:\t\t ", sum_MRAM)

sum_TRAM = 1/2 * (integrand(a) + integrand(b))
for i in range(1,N):
    sum_TRAM += integrand(x = a + i*dx)
sum_TRAM *= dx
print("Trapezoid Riemann Sum:\t\t ", sum_TRAM)

I = integrand(a) + integrand(b) # edge cases
for i in range(1, N, 2): # odd cases
    I += 4*integrand(a + i*dx)
for i in range(2, N, 2): # even cases
    I += 2*integrand(a + i*dx)
I *= dx/3 
print("Simp Rule Integral Approximation:", I)

print("Analytical Value:\t\t ", 2*math.log(2) -3/4)

#####################################################################
print("\nProblem 2:_______")

file = open('HW2-problem2.txt', 'w')

values = []
for i in range(1001):
    values.append(i*0.01)
for j in values:
    dsin = (math.sin(j+0.01) - math.sin(j-0.01))/(2*0.01)
    print(round(j, 2), round(math.sin(j), 4), round(dsin, 4), sep = ' ', end = '\n', file = file)
print("Values generated.")
file.close()
print("problem2.csv is ready with the generated data.")

#####################################################################
print("\nProblem 3:_______")

def f(x):
    return math.exp(x) - 1.2 - 2*x**2

a = 0
b = 3
tolerance = 10**(-5)
dx = abs(b-a)

i=0
while(dx>tolerance):
    i+=1
    mid = (a+b)/2
    if(f(mid) == 0):
        dx=tolerance
    elif(f(a)*f(mid) < 0):
        b = mid
    else:
        a = mid
    dx = abs(b-a)

print("Bisection Method found a zero at x =", (b+a)/2, "in", i, "interations")

def df(x):
    return math.exp(x) - 4*x

x0 = 0.0
tolerance = 10**(-5)
dx = 10*tolerance
i=0

while(dx>tolerance):
    x1 = x0 -f(x0)/df(x0)
    dx = abs(x1 - x0)
    x0 = x1
    i+=1

print('Newton\'s Method found a zero at  x =', x0,'in', i,'interations')
print('Analytical Value:                x = 2.87593')