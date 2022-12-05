import math
import matplotlib.pyplot as plt
print("Program Started:____________________")
print("E Field Section")
# constants
srcPos =   [[0, 0], [ 1, 0]]
srcQ =     [  1,     -1    ]
dL = 0.01
crashRad = 0.05

# functions
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

# main
theta = 0
dTheta = math.radians(15)
Egraph = [[]]*len(srcQ)
while(theta <= 2*math.pi):
    print("theta:", theta)
    notClose = True
    testPos = [dL*math.cos(theta), dL*math.sin(theta)]
    iterations = 0
    while(notClose):
        iterations += 1
        print(iterations)
        dPos = [0,0]
        for i in range(len(dPos)):
            dPos[i] = dL*getEDir(testPos)[i]
        for i in range(len(testPos)):
            testPos[i] += dPos[i]

        # End Condition
        for qPos in srcPos:
            if(qPos != srcPos[0] and disp(testPos, qPos) <= crashRad):
                notClose = False
        if(iterations >= 10):
            notClose = False
    for i in range(len(testPos)):
        Egraph[i].append(testPos[i])
    theta += dTheta

plt.plot(Egraph[0], Egraph[1])
plt.title("E Field Graph")
plt.show()


# print("\nProblem 2:____________________")
# V = [ ]
# n = 50
# for i in range(0,n):
#     temp = [ ]
#     if i==0 or i==n-1:
#         for j in range(0,n):
#             temp.append(1.0)
#     else:
#         for j in range (0,n):
#             temp.append(0.0)
#     V.append(temp)

# for k in range(300):
#     for i in range(1, n-1):
#         for j in range(1, n-1):
#             V[i][j] = 1/4 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])
# x,y,z = [],[],[]
# for i in range(0,n):
#     for j in range(0,n):
#         x.append(i/n)
#         y.append(j/n)
#         z.append(V[i][j])
# print("Graphing Electric Potential For Two Charged Sides")
# plt.figure().add_subplot(111, projection='3d').scatter(x,y,z)
# plt.title('Electric Potential For Two Charged Sides')
# plt.show()