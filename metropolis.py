import math
import random
import matplotlib.pyplot as plt

def gauss(x):
    return math.exp(-x**2)

def metroman(p):
    sigma = 1/math.sqrt(2)
    
    x = []
    N = 10000 # number of x-values
    M = 1000 # number of Monte Carlo steps
    numTrans = []
    for n in range(N):
        x.append(2*random.random() - 1)
        delta = 2
        numTrans.append(0)
        x_new = []
        for i in range(M):
            dx = delta* (2*random.random()-1)
            xi = x[n] + dx
            w = p(xi)/p(x[n])
            if (w >= 1 or w > random.random()):
                x_new.append(xi)
                numTrans[n] += 1
    avg = 0
    for i in range(len(numTrans)):
        avg += numTrans[i]/M
    avg /= N
    print(avg)
    
    plt.hist(x_new, 100,(-1,1))
    plt.show()

metroman(gauss)