import math
import random
import matplotlib.pyplot as plt
import time

t0 = time.time()
S = []
N = 50
M = 20000000
numAve = 0.05*M
temp = []
mag = []

#spins init
for i in range(N):
    S.append([])
    for j in range(N):
        r = random.random()
        if (r>0.5):
            S[i].append(1)
        else:
            S[i].append(-1)

#boundary conditions
for i in range(N):
    for j in range(N):
        if (i == N-1):
            S[i][j] = S[0][j]
        if (j == N-1):
            S[i][j] = S[i][0]

#minus and plus arrays
plus = []
minus = []
for i in range(N):
    plus.append(0)
    minus.append(N-1)
for i in range(N):
    if (i < N-1):
        plus[i] = i+1
    if (i>0):
        minus[i] = i-1

#temperature loop
T = 0.5
while (T <= 3.5):
    print("temp:",T)
    # energy = 0
    mag_t = 0
    Madd = 0
    for i in range(N):
        for j in range(N):
            mag_t += S[i][j]
            # energy -= S[i][j] * (S[i][plus[j]] + S[i][minus[j]] + S[plus[i]][j] + S[minus[i]][j]) 
    for i in range(M):
        ri = random.randint(0,N-1)
        rj = random.randint(0,N-1)
        spinOld = S[ri][rj]

        spinsum = (S[ri][plus[rj]] + S[ri][minus[rj]] + S[plus[ri]][rj] + S[minus[ri]][rj])
        dE = float(2*S[ri][rj]*spinsum)

        if(dE < 0):
            S[ri][rj] = -S[ri][rj]
        elif (math.exp(-dE/T) > random.random()):
            S[ri][rj] = -S[ri][rj]
        if (spinOld != S[ri][rj]):
            # energy += dE
            mag_t += 2*S[ri][rj]
        if(i > M-numAve):
            Madd += mag_t
    
    Madd /= (numAve*N**2)
    mag.append(abs(Madd))
    temp.append(T)
    T += 0.1

print("Code took", round((time.time()-t0),2), "seconds to finish.")
plt.plot(temp, mag, 'o')
plt.show()