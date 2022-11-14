import math
import random
import matplotlib.pyplot as plt

def gauss(x):
    mu = 0
    sigma = 1/math.sqrt(2)
    return 1/(math.sqrt(2*math.pi)*sigma) *math.exp(-(x-mu)**2/(2*sigma**2))

def metroman(p):
    x = []
    N = 10000 # number of x-values
    M = 1000 # number of Monte Carlo steps
    delta = 2.08
    numTrans = []
    print("Monte-Carlo Alg Started...")
    for n in range(N):
        x.append(2*random.random() - 1)
        numTrans.append(0)
        for i in range(M):
            dx = delta* (2*random.random()-1)
            xi = x[n] + dx
            w = p(xi)/p(x[n])
            if (w >= 1 or w >= random.random()):
                x[n] = xi
                numTrans[n] += 1
    print("MC Alg Complete")
    avg = 0
    for i in range(len(numTrans)):
        avg += numTrans[i]/M
    avg /= N
    print(avg)
    
    plt.hist(x, 100,(-3,3))
    plt.show()

metroman(gauss)