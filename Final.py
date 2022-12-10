import math
import matplotlib.pyplot as plt

# constants
    # source charge positions and charges
srcPos = [[0,0], [1,0]]
srcQ = [1, 1]
# srcPos = [[0,0], [3,2], [1,4], [-3,-1]]
# srcQ =   [1, -1, -2, 1]
# srcPos = [[0,0],[1,1],[-0.5,-0.5]]
# srcQ =   [1, -2, 1]
# srcPos = [[0,0]]
# srcQ = [1]

### functions ###
def disp(init, fin):
    rad = 0
    for i in range(len(init)):
        rad += (fin[i]-init[i])**2
    return math.sqrt(rad)

def getEDir(fieldPos):
    E = []
    for i in range(len(fieldPos)): #for each dimension
        En = 0
        for j in range(len(srcQ)): #for each charge
            En += srcQ[j]*(fieldPos[i]-srcPos[j][i])/disp(srcPos[j], fieldPos)**3
        E.append(En)
    EMag = disp(E,[0]*len(E))
    for e in E:
        e /= EMag
        e *= srcQ[0]/abs(srcQ[0])
    return E

# graphing constants
bound_l = 0
bound_r = 0
bound_u = 0
bound_d = 0
for pos in srcPos:
    if(pos[0]-2 < bound_l):
        bound_l = pos[0]-1
    if(pos[0]+2 > bound_r):
        bound_r = pos[0]+1
    if(pos[1]+2 > bound_u):
        bound_u = pos[1]+1
    if(pos[1]-2< bound_d):
        bound_d = pos[1]-1


print("Electric Field Generation")
# """
### e field main ###
dL = 10**-4
crashRad = 0.05
dTheta = math.pi/8
Ex = []
Ey = []
for n in range(len(srcQ)):
    print("\nCharge %d:" %(n))
    theta = dTheta/32
    while(theta <= 2*math.pi):
        print("theta:", theta)
        collide = False
        testPos = [srcPos[n][0] + 0.05/srcQ[n]*math.cos(theta), srcPos[n][1] + 0.05/srcQ[n]*math.sin(theta)]
        iterations = 0
        while(not collide):
            iterations += 1
            EDir = getEDir(testPos)
            
            for i in range(len(EDir)):
                testPos[i] += dL*EDir[i]
            Ex.append(testPos[0])
            Ey.append(testPos[1])

            # End Condition
            for qPos in srcPos:
                if(qPos != srcPos[n] and disp(testPos, qPos) <= crashRad):
                    collide = True
            if(iterations >= 100000):
                collide = True
        print(len(Ex))
        theta += dTheta
print("Graphing Electric Field Plot")
plt.scatter(Ex, Ey, s=1)
charges = [[],[]]
for i in range(len(srcQ)):
    lbl = "q = " + str(srcQ[i]) + "Q"
    plt.scatter(srcPos[i][0], srcPos[i][1], label=lbl)
plt.title("Electric Field Graph")
plt.xlim(bound_l, bound_r)
plt.ylim(bound_d, bound_u)
plt.legend()
plt.show()

# """

print("Equipotential Generation") #################################################
rMax = 0
for pos in srcPos:
    if (disp(pos, srcPos[0]) > rMax):
        rMax = disp(pos, srcPos[0])
dL = 10**-4
r = 0.1
dr = 0.25
crashRad = 0.01
Vx = []
Vy = []
for n in range(len(srcQ)):
    print("\nCharge %d:" %(n))
    r = 0.1
    while(r <= rMax +1):
        print("r:", r)
        connect = False
        initPos = [srcPos[n][0] + r/srcQ[0], srcPos[n][1] + 0]
        testPos = [srcPos[n][0] + r/srcQ[0], srcPos[n][1] + 0]
        iterations = 0
        while(not connect):
            iterations += 1
            EDir = getEDir(testPos)
            VDir = [-EDir[1], EDir[0]]
            
            for i in range(len(VDir)):
                testPos[i] += dL*VDir[i]
            Vx.append(testPos[0])
            Vy.append(testPos[1])

            # End Condition
            for qPos in srcPos:
                if( iterations > 1000 and disp(testPos, initPos) <= crashRad): # how to write connection condition
                    connect = True
            if(iterations >= 100000):
                connect = True
        r = round(r + dr,2)

print("Graphing Equipotential Plot")
plt.scatter(Vx, Vy, s=1)
for i in range(len(srcQ)):
    lbl = "q = " + str(srcQ[i]) + "Q"
    plt.scatter(srcPos[i][0], srcPos[i][1], label=lbl)
plt.title("Equipotential Lines Graph")
plt.legend()
plt.xlim(bound_l, bound_r)
plt.ylim(bound_d, bound_u)
plt.show()
# """