def f(x):
    y = x
    return y
a = 1
b = 1
N = 10
dx = (b-a)/N

I = f(a) + f(b) # edge cases
for i in range(1, N, 2): # odd cases
    I += 4*f(a + i*dx)
for i in range(2, N, 2): # even cases
    I += 2*f(a + i*dx)
I *= dx/3 

print("Simp Rule Integral Approximation:", I, end = " ")