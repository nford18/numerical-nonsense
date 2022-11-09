import random as rand

# Exercise 1
N = 100000
n = 0
for i in range(N): 
    x = rand.random()
    y = rand.random()
    if(y <= x**3):
        n += 1
print(n/N)

#Exercise 2
n = 0
for i in range(N):
    x = 2*rand.random()-1
    y = 2*rand.random()-1
    z = rand.random()
    if(x**2 + y**2 <= 1 and z <= 1/2):
        n += 1
print(n/N)