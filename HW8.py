import math
import random
import matplotlib.pyplot as plt

def metroman(p,delta, a, D=1,N=10000, M=1000, pos=[]):
    numTrans = 0
    print("Monte-Carlo Alg Started...")
    for n in range(N):
        for i in range(M):
            xi = []
            mag = 0
            magi = 0
            for d in range(D):
                dx = delta* (2*random.random()-1)
                xi.append(abs(pos[d][n] + dx))
                mag += pos[d][n]**2
                magi += xi[d]**2
            mag  = math.sqrt(mag)
            magi = math.sqrt(magi)
            w = p(magi,a)/p(mag,a)
            if (w > 1 or w > random.random()):
                for d in range(D):
                    pos[d][n] = xi[d]
                numTrans += 1
    print("MC Alg Complete")
    print("Average num of transitions:", numTrans/M/N)

print("Problem 1:______________________________")
def hydrogen1d(r, alpha):
    return r**2 * math.exp(-2*alpha*abs(r))

alphas = [0.50, 0.75, 1.00, 1.25, 1.50]
EList = []
N = 10000 
M = 100
for a in alphas:
    print("\tFor \u03B1 =", a)
    E = 0
    rList = [0.5] * N
    metroman(hydrogen1d, 5/a, a, M=M, pos=[rList])
    for i in range(N):
        E += -a**2 /2 + (a-1)/rList[i]
    EList.append(E/N)
plt.plot(alphas, EList)
plt.title("1d Random Walker Solution")
plt.show()

print("\n\nProblem 2:______________________________")
def hydrogen3d(r, alpha):
    return math.exp(-2*alpha*r)
alphas = [0.50, 0.75, 1.00, 1.25, 1.50]
EList = []
N = 10000
M = 100
for a in alphas:
    print("\tFor \u03B1 =", a)
    E = 0
    rList = [[0.5]*N, [0.5]*N, [0.5]*N]
    metroman(hydrogen3d, 1.5/a, a, M=M, pos=rList, D=3)
    for i in range(N):
        E += -a**2 /2 + (a-1)/math.sqrt(rList[0][i]**2 + rList[1][i]**2 + rList[2][i]**2)
    EList.append(E/N)
plt.plot(alphas, EList)
plt.title("3d Random Walker Solution")
plt.show()