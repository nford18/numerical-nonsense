import math
# import matplotlib.pyplot as plt
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
print(E)
EMag = math.sqrt(E[0]**2 + E[1]**2 + E[2]**2)
print("The magnitude of the Electric Field is:", EMag)
print("The direction of the E Field is:", round(E[0]/EMag, 4),"\b\u0078\u0302 +",round(E[1]/EMag, 4),"\b\u0177 +",round(E[2]/EMag, 4),"\b\u1E91")

print("Problem 2:____________________")