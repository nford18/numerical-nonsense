import math
import matplotlib.pyplot as plt

### Tester source charge positions and charges
# srcPos = [[-1,0], [1,0]]
# srcQ = [1, 1]
# srcPos = [[0,0], [3,2], [1,4], [-3,-1]]
# srcQ =   [1, -1, -2, 1]
srcPos = [[0,math.sqrt(3)],[1,0],[-1,0]]
srcQ =   [3, 3, 3]
# srcPos = [[0,0]]
# srcQ = [1]

### functions ###
def disp(init, fin): # finds the displacement between two positions.
    rad = 0
    for i in range(len(init)):
        rad += (fin[i]-init[i])**2 
    return math.sqrt(rad)

# finds the direction of the electric field at a given point due to the source charges specified above.
def getEDir(fieldPos, n): # takes a position and the number of the source charge to consider signs
    E = []
    for i in range(len(fieldPos)): #for each dimension
        En = 0
        for j in range(len(srcQ)): #for each charge
            En += srcQ[j]*(fieldPos[i]-srcPos[j][i])/disp(srcPos[j], fieldPos)**3
        E.append(En)
        
    EMag = disp(E,[0]*len(E)) # magnitude of generated electric field vector
    for e in E: #
        e /= EMag
        e *= srcQ[n]/abs(srcQ[n])
    return E

# graphing constants to center plot on charges
bound_l = 0
bound_r = 0
bound_u = 0
bound_d = 0
for pos in srcPos:
    # finds the highest and lowest x- and y-coords and sets the bounds one farther than them
    if(pos[0]-2 < bound_l):
        bound_l = pos[0]-1
    if(pos[0]+2 > bound_r):
        bound_r = pos[0]+1
    if(pos[1]+2 > bound_u):
        bound_u = pos[1]+1
    if(pos[1]-2< bound_d):
        bound_d = pos[1]-1

print("Electric Field Generation") #################################################
dL = 10**-4 # incremental distance
crashRad = 0.05 # end loop condition (how close to the other charges the plot gets)
dTheta = math.pi/8 # angle increment
Ex = [] # arrays to hold x and y 'positions' of points along field lines 
Ey = []
for n in range(len(srcQ)): # drawing lines from each source charge
    print("Drawing From Charge %d..." %(n+1))
    theta = dTheta/32 # initial angle 
    while(theta <= 2*math.pi): 
        collide = False # initialize end condition for each loop iteration
        iterations = 0  # failsafe end condition in case other is not met
        testPos = [srcPos[n][0] + 0.05*math.cos(theta), srcPos[n][1] + 0.05*math.sin(theta)] # initalize test position
        while(not collide and iterations < 200000):
            iterations += 1
            EDir = getEDir(testPos, n)  # fetch direction of E at point
            for i in range(len(EDir)):
                testPos[i] += dL*EDir[i] # move x and y in respective directions by dl distance
            Ex.append(testPos[0]) # append new points to array
            Ey.append(testPos[1])

            # End Condition
            for qPos in srcPos:
                # if any of the source charges are within the given 'crash radius' from the test position end iteration
                # for current angle
                if(qPos != srcPos[n] and disp(testPos, qPos) <= crashRad): 
                    collide = True
        theta += dTheta
print("Graphing Electric Field Plot")
plt.scatter(Ex, Ey, s=1)
# adds charges to the plot {
for i in range(len(srcQ)):
    lbl = "q = " + str(srcQ[i]) + "Q"
    plt.scatter(srcPos[i][0], srcPos[i][1], label=lbl)
# }
plt.title("Electric Field Graph")
plt.xlim(bound_l, bound_r)
plt.ylim(bound_d, bound_u)
plt.legend(loc='upper right')
plt.show()

print("\nEquipotential Generation") #################################################
dL = 10**-4 # incremental distance
crashRad = 0.1 # radius for connection of equipotential lines
Vx = [] # arrays to hold x and y 'positions' of points along equipotential lines
Vy = []
for n in range(len(srcQ)):# drawing lines from each source charge
    print("Drawing From Charge %d..." %(n+1))
    # finds the closest other source charge and uses that distance as the maximum radius 
    # this is to avoid overlap of lines as much as possible b/c it clutters the plot
    rMax = 500
    for i in range(len(srcPos)):
        temp = disp(srcPos[i], srcPos[n])
        if (temp != 0.0 and temp < rMax): # test for if current distance is less than and is not ~0 (would happen...
            rMax = temp                   # ...for the distance between point and itself)
    r = 0.075 # initialize radius 
    dr = round((rMax-r)/10, 2) # radius increment based on rMax for the current source
    while(r < rMax):
        connect = False # initialize end condition for each loop iteration
        iterations = 0  # failsafe end condition in case other is not met
        initPos = [srcPos[n][0] + r, srcPos[n][1] + 0] # initial position
        testPos = [srcPos[n][0] + r, srcPos[n][1] + 0] # initalize test position with same value
        while(not connect and iterations < 100000):
            iterations += 1
            EDir = getEDir(testPos, n)    # fetch direction of E at point
            VDir = [-EDir[1], EDir[0]] # E direction rotated 90 degrees CCW
            for i in range(len(VDir)):
                testPos[i] += dL*VDir[i] # move x and y in respective directions by dl distance
            Vx.append(testPos[0]) # append new points to array
            Vy.append(testPos[1])

            # End Condition
            for qPos in srcPos:
                # if the test point comes within the given 'crash radius' from the starting position after a number of
                # iterations, end iteration for current radius
                if(iterations > 2000 and disp(testPos, initPos) <= crashRad):
                    connect = True
        r = round(r + dr,2) # incrementation is rounded because float addition is inaccurate
print("Graphing Equipotential Plot")
plt.scatter(Vx, Vy, s=1)
# adds charges to the plot {
for i in range(len(srcQ)):
    lbl = "q = " + str(srcQ[i]) + "Q"
    plt.scatter(srcPos[i][0], srcPos[i][1], label=lbl)
# }
plt.title("Equipotential Lines Graph")
plt.legend(loc='upper right')
plt.xlim(bound_l, bound_r)
plt.ylim(bound_d, bound_u)
plt.show()

print("\nGraphing Overlayed Plot") #################################################
# Optional plot to overlay the Field lines and Equipotential lines
plt.scatter(Ex, Ey, s=1, label='Electric Field Lines')
plt.scatter(Vx, Vy, s=1, label='Potential Lines')
for i in range(len(srcQ)):
    lbl = "q = " + str(srcQ[i]) + "Q"
    plt.scatter(srcPos[i][0], srcPos[i][1], label=lbl)
plt.title("Overlay of Both Graphs")
plt.legend(loc='best')
plt.xlim(bound_l, bound_r)
plt.ylim(bound_d, bound_u)
plt.show()