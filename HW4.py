import math
import matplotlib.pyplot as pyplot

# Overall Constants
tol = 5*10**(-4)
dt = 0.001
g = 9.8

print("Problem 1:________________________________________")
def dragAccel(vy, mass, c1, c2):
    return -g - (c1/mass)*vy - (c2/mass)*vy*abs(vy)
def mechEnergy(m, v, h):
    return 0.5*m*v**2 + m*g*h
c1 = 0.1
c2 = 0
m = 0.1
y0 = 50
v0 = 0.1
a0 = -g

pos = []
y = y0
vel = []
v = v0
acc = []
time = []

# creation of position and velocity arrays
for i in range(0,int(10/dt)):
    acc.append(dragAccel(v,m,c1,c2))
    v += acc[i]*dt
    vel.append(v)
    y += v*dt
    pos.append(y)
    time.append(i*dt)
    if(pos[i] <= tol):
        break

# question tests
landTime = 0
maxHTime = 0
isTerminal = False
isSame = 0
for i in range(0, len(time)):
    if(maxHTime == 0 and vel[i] <= 0):
        maxHTime = i - 1
        print("Maximum Height: y =", pos[i],"m")
    
    if((not isTerminal) and abs(acc[i-1] - 0) < tol): # terminal velocity test
        isTerminal = True
        print("Terminal Velocity: v =", v, "m/s")
    if(i == len(time) - 1 and isTerminal == False):
        print("Terminal Velocity is not met before impact.")
    
    if(landTime == 0 and pos[i] <= 0):
        landTime = i - 1
        print("Hit Ground Time: t =", time[landTime], "s")
        print("Velocity at Impact: v =", vel[landTime], "m/s")
print("Initial Total Mechanical Energy: E=", mechEnergy(m,vel[0],pos[0]), "J")
print("Final Total Mechanical Energy: E=", mechEnergy(m,vel[landTime],pos[landTime]), "J")    

pyplot.plot(time, pos, label='Linear c: y vs. t')
pyplot.legend()
pyplot.show()
pyplot.plot(time, vel, label='Linear c: v vs. t')
pyplot.legend()
pyplot.show()
pyplot.plot(time, acc, label='Linear c: a vs. t')
pyplot.legend()
pyplot.show()

print("\nProblem 2:________________________________________")
c1 = 0
c2 = 0.1
pos = []
y = y0
vel = []
v = v0
acc = []
time = []

# creation of position and velocity arrays
for i in range(0,int(20/dt)):
    acc.append(dragAccel(v,m,c1,c2))
    v += acc[i]*dt
    vel.append(v)
    y += v*dt
    pos.append(y)
    time.append(i*dt)
    if(pos[i] <= tol):
        break

# question tests
landTime = 0
maxHTime = 0
isTerminal = False
for i in range(0, len(time)):
    if(maxHTime == 0 and vel[i] <= 0):
        maxHTime = i - 1
        print("Maximum Height: y =", pos[i],"m")
    
    if((not isTerminal) and abs(acc[i-1] - 0) < tol): # terminal velocity test
        isTerminal = True
        print("Terminal Velocity: v =", v, "m/s")
    if(i == len(time) - 1 and isTerminal == False):
        print("Terminal Velocity is not met before impact.")
    
    if(landTime == 0 and pos[i] <= 0):
        landTime = i - 1
        print("Hit Ground Time: t =", time[landTime], "s")
        print("Velocity at Impact: v =", vel[landTime], "m/s")
print("Initial Total Mechanical Energy: E=", mechEnergy(m,vel[0],pos[0]), "J")
print("Final Total Mechanical Energy: E=", mechEnergy(m,vel[landTime],pos[landTime]), "J")    

pyplot.plot(time, pos, label='Quadratic c: y vs. t')
pyplot.legend()
pyplot.show()
pyplot.plot(time, vel, label='Quadratic c: v vs. t')
pyplot.legend()
pyplot.show()
pyplot.plot(time, acc, label='Quadratic c: a vs. t')
pyplot.legend()
pyplot.show()

print("\nProblem 3:________________________________________")
def dragAccelX(vx, mass, c1, c2):
    return -(c1/mass)*vx - (c2/mass)*vx*abs(vx)

c1 = 0.08
c2 = 0
m = 0.050
theta = 50
x0 = 0
y0 = 0.1
v0 = 15

xPos = []
x = x0
yPos = []
y = y0
vely = []
vy = v0*math.sin(math.radians(theta))
velx = []
vx = v0*math.cos(math.radians(theta))
time = []

# creation of position and velocity arrays
for i in range(0,int(20/dt)):
    vy += dragAccel(vy,m,c1,c2)*dt
    vely.append(vy)
    y += vy*dt
    yPos.append(y)
    vx += dragAccelX(vx,m,c1,c2)*dt
    velx.append(vx)
    x += vx*dt
    xPos.append(x)
    time.append(i*dt)
    if(yPos[i] <= tol):
        break

landTime = 0
maxHTime = 0
for i in range(0, len(time)):   
    if(maxHTime == 0 and vely[i] <= 0):
        maxHTime = i - 1
        print("Maximum Height: y =", yPos[i],"m")

    if(landTime == 0 and yPos[i] <= 0):
        landTime = i - 1
        print("Time of flight: t =", time[landTime], "s")
print("Horizontal Range: x =", xPos[-1],"m")

pyplot.plot(xPos, yPos, label='Range with Linear Drag: y vs. x')
pyplot.legend()
pyplot.show()