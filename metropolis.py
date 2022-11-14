import math
import random
import matplotlib.pyplot as plt

def gauss(x):
    mu = 0
    sigma = 1/math.sqrt(2)
    return 1/(math.sqrt(2*math.pi)*sigma) *math.exp(-(x-mu)**2/(2*sigma**2))

def MC_test(p):
    x = []
    N = 10000 # number of x-values
    M = 1000 # number of Monte Carlo steps
    sigma = 1/math.sqrt(2) # standard deviation
    delta = 2.08
    numTrans = []
    oneStdev = 0
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
        if abs(x[n]) < sigma:
            oneStdev += 1 
    print("MC Alg Complete")
    avg = 0
    for i in range(len(numTrans)):
        avg += numTrans[i]/M
    avg /= N
    print("Percent inside 1\u03C3:", 100*oneStdev/N, "\b%")
    print("Average number of transitioned points:", avg)
    
    
    plt.hist(x, bins=100, density=True)
    plt.show()

# MC_test(gauss)

def metroman(p,D):
    pos = []
    for i in range(D):
        pos.append([])
    N = 10000 # number of x-values
    M = 1000 # number of Monte Carlo steps
    delta = 2.08
    numTrans = []
    print("Monte-Carlo Alg Started...")
    for d in range(D):
        for n in range(N):
            pos[d].append(2*random.random() - 1)
            numTrans.append(0)
            for i in range(M):
                dx = delta* (2*random.random()-1)
                xi = pos[d][n] + dx
                w = p(xi)/p(pos[d][n])
                if (w >= 1 or w >= random.random()):
                    pos[d][n] = xi
                    numTrans[n] += 1
        print("MC Alg Complete")
        avg = 0
        for i in range(len(numTrans)):
            avg += numTrans[i]/M
        avg /= N
        print("Average number of transitioned points:", avg)
    return pos
data = metroman(gauss, 1)
plt.figure().add_subplot(projection='3d').scatter(data[0],data[1],data[2])
plt.show()
