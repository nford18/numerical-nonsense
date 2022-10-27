import math
import matplotlib.pyplot as pyplot

print("Problem 1:________________________________________")

x0 = 10
y0 = 0
vc = 1/math.sqrt(x0)
v0 = [0,0.3*vc]
E0 = 1/2 * v0[1]**2 - 1/x0
l0 = x0*v0[1]

a = 1/(2/x0 - v0[1]**2)
alpha = l0**2 
epsilon = math.sqrt(1-l0**2/a)
T = 2*math.pi*a**(3/2)

def r_anl(theta):
    return alpha/(1+epsilon*math.cos(theta))

#analytical
#############################
print("Analytical Plot Started...")
theta = 0
dtheta = 0.001
x_anl = []
y_anl = []
while (theta < 2*math.pi):
    theta += dtheta
    x_anl.append(x0-alpha/(1+epsilon)+r_anl(theta)*math.cos(theta))
    y_anl.append(r_anl(theta)*math.sin(theta))
# pyplot.plot(x_anl, y_anl, label='Analytical Sol.')
# pyplot.legend()
# pyplot.show()
#############################

def accel(x,y):
    ax = -x/(math.sqrt(x**2+y**2)**3)
    ay = -y/(math.sqrt(x**2+y**2)**3)
    return [ax,ay]
def mechE(v, r):
    return 0.5*v**2 - 1/r

# Runge-Kutta 2nd Order
#############################
print("\nRunge-Kutta Evolution Started...")
t = 0
dt = 0.001
pos = [x0,y0]
v_rk = [v0[0], v0[1]]
x_rk = []
y_rk = []
energy_rk = []
l_rk = []
time_rk = []

while(t <= 5*T):
    acc = accel(pos[0],pos[1])
    acc_next = accel(pos[0] + dt/2*v_rk[0], pos[1] + dt/2*v_rk[1])
    for i in range(2):
        pos[i] += v_rk[i]*dt + acc[i]/2*dt**2
        v_rk[i] += dt/2*(acc_next[i])
    x_rk.append(pos[0])
    y_rk.append(pos[1])
    
    v = math.sqrt(v_rk[0]**2 + v_rk[1]**2)
    r = math.sqrt((pos[0]-x0/2)**2 + (pos[1]-y0/2)**2)
    energy_rk.append(mechE(v, r))
    l_rk.append(pos[0]*v_rk[1]-pos[1]*v_rk[0])
    time_rk.append(t)
    t += dt
# pyplot.plot(x_rk, y_rk, label='Runge-Kutta 2nd Order Evolution')
# pyplot.legend()
# pyplot.show()
print("The 2nd Order Runge-Kutta Approximation does not yield a closed orbit and has a processesing orbit.")
#############################

# Velocity-Verlet
#############################
print("\nVelocity-Verlet Evolution Started...")
t = 0
dt = 0.001
pos = [x0,y0]
v_vv = [v0[0], v0[1]]
x_vv = []
y_vv = []
energy_vv = []
l_vv = []
time_vv = []

while(t <= 5*T):
    acc = accel(pos[0],pos[1])
    acc_next = accel(pos[0] + v_vv[0]*dt + acc[0]/2*dt**2, pos[1] + v_vv[1]*dt + acc[1]/2*dt**2)
    for i in range(2):
        pos[i] += v_vv[i]*dt + acc[i]/2*dt**2
        v_vv[i] += dt/2*(acc_next[i]+acc[i])
    x_vv.append(pos[0])
    y_vv.append(pos[1])

    v = math.sqrt(v_vv[0]**2 + v_vv[1]**2)
    r = math.sqrt((pos[0]-x0/2)**2 + (pos[1]-y0/2)**2)
    energy_vv.append(mechE(v, r))
    l_vv.append(pos[0]*v_vv[1]-pos[1]*v_vv[0])
    time_vv.append(t)
    t += dt
# pyplot.plot(x_vv, y_vv, label='Velocity Verlet Evolution')
# pyplot.legend()
# pyplot.show()
print("The Velocity-Verlet Approximation seems to yield a closed orbit and without a processesing orbit.")
#############################
print("\nGraphing Energy per Unit Mass functions...")
# pyplot.plot(time_rk, energy_rk, label='RK Energy/mass v Time')
# pyplot.legend()
# pyplot.show()
# pyplot.plot(time_vv, energy_vv, label='V-V Energy/mass v Time')
# pyplot.legend()
# pyplot.show()
print("Graphing Angular Momentum per Unit Mass functions...")
# pyplot.plot(time_rk, l_rk, label='RK Angular Momentum/mass v Time')
# pyplot.legend()
# pyplot.show()
# pyplot.plot(time_vv, l_vv, label='V-V Angular Momentum/mass v Time')
# pyplot.legend()
# pyplot.show()
print("As expected the Total Mechanical Energy and Angular Momentum plots are much more accurate to the \ntheoretical perfect"
" elliptical orbit with the Velocity-Verlet Evolution than with the 2nd Order \nRunge-Kutta Evolution. This was expected due to the V-V"
" approximation's accuracy to an analytically \nobtained elliptical orbit.")

################################################################################################
print("\n\nProblem 2:________________________________________")
def accel2(x,y):
    r = [x,y]
    R = [0.5,0.0]
    acc2 = []
    for i in range(2):
        a1 = -0.5*(r[i]-R[i])/(math.sqrt((r[0]-R[0])**2 + (r[1]-R[1])**2)**3)
        a2 = -0.5*(r[i]+R[i])/(math.sqrt((r[0]+R[0])**2 + (r[1]+R[1])**2)**3)
        acc2.append(a1 + a2)
    return acc2

# Evolution
print("3-Body Velocity-Verlet Evolution Started...")
v0=0.9
theta0 = math.radians(39)
t = 0
dt = 0.001
pos = [0.0,0.0]
v_3b1 = [v0*math.cos(theta0), v0*math.sin(theta0)]
x_3b1 = []
y_3b1 = []
time_3b1 = []

while(t <= 1*T):
    acc = accel2(pos[0],pos[1])
    acc_next = accel2(pos[0] + v_3b1[0]*dt + acc[0]/2*dt**2, pos[1] + v_3b1[1]*dt + acc[1]/2*dt**2)
    for i in range(2):
        pos[i] += v_3b1[i]*dt + acc[i]/2*dt**2
        v_3b1[i] += dt/2*(acc_next[i]+acc[i])
    x_3b1.append(pos[0])
    y_3b1.append(pos[1])    
    time_3b1.append(t)
    t += dt
print("The maximum timestep I found before the object escaped from orbit happened was 0.015 s.")
print("The values for v_0 and theta that I found were 0.9 m/s at 39 degrees from +x axis.")
# pyplot.plot(x_3b1, y_3b1, label='3-Body Velocity Verlet Evolution')
# pyplot.legend()
# pyplot.show()


################################################################################################
print("\n\nProblem 3:________________________________________")
def accel3(x,y,t):
    r = [x,y]
    R1 = [-0.5*math.cos(t),-0.5*math.sin(t)]
    R2 = [0.5*math.cos(t),0.5*math.sin(t)]
    acc3 = []
    for i in range(2):
        a1 = -0.5*(r[i]-R1[i])/(math.sqrt((r[0]-R1[0])**2 + (r[1]-R1[1])**2)**3)
        a2 = -0.5*(r[i]-R2[i])/(math.sqrt((r[0]-R2[0])**2 + (r[1]-R2[1])**2)**3)
        acc3.append(a1 + a2)
    return acc3

# Velocity-Verlet
#############################
print("3-Body w/ Rotating Centers Velocity-Verlet Evolution Started...")
t = 0
dt = 0.001
pos = [0.0,0.058]
v0=0.49
theta0 = math.radians(0)
v_3b2 = [v0*math.cos(theta0), v0*math.sin(theta0)]
x_3b2 = []
y_3b2 = []
rotPos = [[],[]]
time_3b2 = []

while(t <= 1*T):
    acc = accel3(pos[0],pos[1],t)
    acc_next = accel3(pos[0] + v_3b2[0]*dt + acc[0]/2*dt**2, pos[1] + v_3b2[1]*dt + acc[1]/2*dt**2,t)
    for i in range(2):
        pos[i] += v_3b2[i]*dt + acc[i]/2*dt**2
        v_3b2[i] += dt/2*(acc_next[i]+acc[i])
    x_3b2.append(pos[0])
    y_3b2.append(pos[1])    
    rotPos[0].append(x_3b2[int(t/dt)]*math.cos(t) + y_3b2[int(t/dt)]*math.sin(t))
    rotPos[1].append(-x_3b2[int(t/dt)]*math.sin(t) + y_3b2[int(t/dt)]*math.cos(t))
    time_3b2.append(t)
    t += dt
pyplot.plot(x_3b2, y_3b2, label='3-Body, Rot. Centers V-V Evo\nLab Frame')
pyplot.legend()
pyplot.show()
pyplot.plot(rotPos[0], rotPos[1], label='3-Body, Rot. Centers V-V Evo\nRotating Frame')
pyplot.legend()
pyplot.show()

print("Chaotic Orbit achieved with v0 = [0.2954,0.0521], x0 = [0.000, 0.058]")
print("Ionization achieved with v0 = [0.9,0.0], x0 = [0.000, 0.058]")
################################################################################################
print("\nFinished\n")