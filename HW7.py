import math
import matplotlib.pyplot as plt
print("Problem 1:____________________")
#functions
def displ(init, fin):
    return math.sqrt((fin[0]-init[0])**2 + (fin[1]-init[1])**2 +(fin[2]-init[2])**2)

#constants
srcPos =   [[-1, 1, 2], [ 2, 1,-1], [ 1, 1, 1]]
srcQ =     [    -2,         -1,          1    ]
fieldPos =  [ 3, 2, 1]

V = 0
E = []
for i in range(len(srcQ)):
    V += srcQ[i]/ displ(srcPos[i], fieldPos)
print("Value of Electric Potential is:", V)

for i in range(len(fieldPos)): #for each dimension
    En = 0
    for j in range(len(srcQ)): #for each charge
        En += srcQ[j]*(fieldPos[i]-srcPos[j][i])/displ(srcPos[j], fieldPos)**3
    E.append(En)
EMag = math.sqrt(E[0]**2 + E[1]**2 + E[2]**2)
print("The magnitude of the Electric Field is:", EMag)
print("The direction of the E Field is:", round(E[0]/EMag, 4),"\bi\u0302 +",round(E[1]/EMag, 4),"\bj\u0302 +",round(E[2]/EMag, 4),"\bk\u0302")
print("\t^^These calculations were done with units of k = 1 kg*m^3*s^-4*A^-2 and Q = 1 C")

print("\nProblem 2:____________________")
V = [ ]
n = 50
for i in range(0,n):
    temp = [ ]
    if i==0 or i==n-1:
        for j in range(0,n):
            temp.append(1.0)
    else:
        for j in range (0,n):
            temp.append(0.0)
    V.append(temp)

for k in range(300):
    for i in range(1, n-1):
        for j in range(1, n-1):
            V[i][j] = 1/4 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])
x,y,z = [],[],[]
for i in range(0,n):
    for j in range(0,n):
        x.append(i/n)
        y.append(j/n)
        z.append(V[i][j])
print("Graphing Electric Potential For Two Charged Sides")
plt.figure().add_subplot(111, projection='3d').scatter(x,y,z)
plt.title('Electric Potential For Two Charged Sides')
plt.show()

print("\nProblem 3:____________________")
V = [ ]
n = 50
for i in range(0,n):
    temp = [ ]
    if i==0:
        for j in range(0,n):
            temp.append(1.0)
    else:
        for j in range (0,n):
            temp.append(0.0)
    V.append(temp)

for k in range(300):
    for i in range(1, n-1):
        for j in range(1, n-1):
            V[i][j] = 1/4 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])
x,y,z = [],[],[]
for i in range(0,n):
    for j in range(0,n):
        x.append(i/n)
        y.append(j/n)
        z.append(V[i][j])
print("Graphing Electric Potential For One Charged Side")
plt.figure().add_subplot(111, projection='3d').scatter(x,y,z)
plt.title('Electric Potential For One Charged Side')
plt.show()