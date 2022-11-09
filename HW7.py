import matplotlib.pyplot as plt
import math
print("Problem 1:____________________")
#functions
def displ(init, fin):
    return math.sqrt((fin[0]-init[0])**2 + (fin[1]-init[1])**2 +(fin[2]-init[2])**2)


#constants
sourcePos = [[-1,1,2], [2,1,-1], [1,1,1]]
sourceQ =   [   -2,      -1,        1   ]
fieldPos = [3,2,1]

V = 0
for i in range(3):
    V += sourceQ[i]/ displ(sourcePos[i], fieldPos)
print("Value of Electric Potential is:", V)



