import math
import random
import matplotlib.pyplot as plt
import metropolis as mtr

def metroman(p,delta, a, D=1,N=10000, M=1000, pos=[]):
    if(len(pos) == 0):
        for i in range(D):
            pos.append([])
    numTrans = []
    print("Monte-Carlo Alg Started...")
    for d in range(D):
        for n in range(N):
            if(len(pos[d]) == 0):
                pos[d].append(2*random.random() - 1)
            numTrans.append(0)
            for i in range(M):
                dx = delta* (2*random.random()-1)
                xi = abs(pos[d][n] + dx)
                w = p(xi,a)/p(pos[d][n],a)
                if (w > 1 or w > random.random()):
                    pos[d][n] = xi
                    numTrans[n] += 1
        print("MC Alg Complete")
        avg = 0
        for i in range(len(numTrans)):
            avg += numTrans[i]/M
        avg /= N
        print("Average number of transitioned points:", avg)
"""
print("Problem 1:______________________________")
def hydrogen1d(r, alpha):
    return r**2 * math.exp(-2*alpha*abs(r))


alphas = [0.50, 0.75, 1.00, 1.25, 1.50]
EList = []
for a in alphas:
    E = 0
    N = 10000
    M = 100
    rList = [0.5] * N
    metroman(hydrogen1d, 4/a, a, M=M, pos=[rList])
    for i in range(N):
        E += -a**2 /2 + (a-1)/rList[i]
    EList.append(E/N)
    print(EList)
plt.plot(alphas, EList)
plt.show()
"""
print("Problem 2:______________________________")
def metroman2(p,delta, a, D=1,N=10000, M=1000, pos=[]):
    if(len(pos) == 0):
        for i in range(D):
            pos.append([])
    numTrans = []
    print("Monte-Carlo Alg Started...")
    for d in range(D):
        numTrans = []
        for n in range(N):
            if(len(pos[d]) == 0):
                pos[d].append(2*random.random() - 1)
            numTrans.append(0)
            for i in range(M):
                dx = delta* (2*random.random()-1)
                xi = []
                for d in range(D):
                    xi.append(abs(pos[d][n] + dx))
                mag  = math.sqrt(pos[d][n]**2 + pos[d][n]**2 + pos[d][n]**2)
                magi = math.sqrt(xi[0]**2 + xi[1]**2 + xi[2]**2)
                w = p(magi,a)/p(mag,a)
                if (w > 1 or w > random.random()):
                    for d in range(D):
                        pos[d][n] = xi[d]
                    numTrans[n] += 1
        print("MC Alg Complete")
        avg = 0
        for i in range(len(numTrans)):
            avg += numTrans[i]/M
        avg /= N
        print("Average number of transitioned points:", avg)

def hydrogen3d(r, alpha):
    return math.exp(-2*alpha*r)
alphas = [0.50, 0.75, 1.00, 1.25, 1.50]
EList = []
for a in alphas:
    E = 0
    N = 10000
    M = 100
    rList = [[0.5]*N, [0.5]*N, [0.5]*N]
    metroman(hydrogen3d, 2.1/a, a, M=M, pos=rList, D=3)
    for i in range(N):
        E += -a**2 /2 + (a-1)/math.sqrt(rList[0][i]**2 + rList[1][i]**2 + rList[2][i]**2)
    EList.append(E/N)
    print(EList)
plt.plot(alphas, EList)
plt.show()