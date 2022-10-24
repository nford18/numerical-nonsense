import math
import numpy
import matplotlib.pyplot as plt


print("\nProblem 1:__________")
#constants
g = 9.8 # gravitational acceleration
v_0S = 15.0 # small object initial velocity
y_0L = 10.0 # large object initial position
v_0L = -0.2 # large object initial velocity
c = 0.1     # large object air resistance constant

def yL(t):
    return y_0L - g/c*t + 1/c*(v_0L + g/c)*(1-math.exp(-c*t))

def yS(t):
    return v_0S*t - g/2*t**2

def f(t):
    return yL(t) - yS(t)
    # return y_0L - (v_0S + g/c)*t + g/2*t**2 + 1/c*(v_0L + g/c)*(1-math.exp(-c*t))

def dyL(t):
    # uses center difference method
    dt = 0.001
    return (yL(t+dt) - yL(t-dt))/(2*dt)
    #expected result: v
    # return -g/c + (v_0L + g/c)*math.exp(-c*t)

def dyS(t):
    return v_0S -g*t

def df(t):
    # return dyL(t) - dyS(t)
    return -(v_0S + g/c) + g*t + (v_0L + g/c)*(math.exp(-c*t))

# Newton's method for solving
t0 = 1.875 
tol = 10**(-5)
dt = 10*tol

while(dt>tol):
    t1 = t0 -f(t0)/df(t0)
    dt = abs(t1 - t0)
    t0 = t1

print("The objects meet at t = ", t0)
print("The small object has flown ", yS(t0),"m")
print("The large object has dropped ", yL(t0), "m")

time = numpy.arange(0,1.531,0.001)
y1 = numpy.array([])
y2 = numpy.array([])
for i in time:
    y1 = numpy.append(y1, yS(i))
    y2 = numpy.append(y2, yL(i))
    
plt.plot(time,y1, label='Small Object')
plt.plot(time,y2, label='Large Object')
plt.legend()
print("Position of the two objects: Plotted.")
plt.show()

print("The small object has velocity: ", dyS(t0),"m/s")
print("The large object has velocity: ", dyL(t0), "m/s")

print("\nProblem 2:__________")

def vx(t, t0):
    return -0.01*(t*math.log((1+t)/(1+t0))-(1+t) +math.log(abs(1+t))) + 0.84
def dvx_num(t,t0):
    dt = 0.001
    return (vx(t+dt,t0) - vx(t-dt,t0))/(2*dt)

def dvx_anl(t,t0):
    return -0.01*math.log((1+t)/(1+t0))

time = numpy.arange(0,10,0.01)
pos = numpy.array([])
accel_num = numpy.array([])
accel_anl = numpy.array([])

a = 0
b = 10
N = 1000
dx = (b-a)/N

sum_MRAM = 0
for i in range(0,N):
    sum_MRAM += dx*vx(a + i*dx + dx/2, 0)
    pos = numpy.append(pos, sum_MRAM)

plt.plot(time, pos, label='x vs. t (MRAM Method)')
plt.legend()
print("Position from MRAM: Plotted.")
plt.show()

for i in time:
    accel_num = numpy.append(accel_num, dvx_num(i,0))
    accel_anl = numpy.append(accel_anl, dvx_anl(i,0))

plt.plot(time, accel_num, label='a vs. t (Center Diff. Method from dv/dt)')
plt.plot(time, accel_anl, label='a vs. t (Analytical)')
plt.legend()
print("Acceleration from Center Difference and Analytical: Plotted.")
plt.show()

acc_MRAM = numpy.array([])
for i in range(0,len(pos)-2):
    dt = 0.001
    dumb = (pos[i+2] - 2*pos[i+1] + pos[i])/(dt**2)
    acc_MRAM = numpy.append(acc_MRAM, dumb)
time = numpy.delete(time, -1)
time = numpy.delete(time, -1)
plt.plot(time, acc_MRAM, label='a vs. t (from MRAM position data)')
plt.legend()
print("Acceleration from MRAM postion data: Plotted")
plt.show()