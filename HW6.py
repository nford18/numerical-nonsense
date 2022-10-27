import math
import numpy
import matplotlib.pyplot as pyplot
import scipy

a = 2.5     # 1/Angstroms
b = 1.162   # Angstroms
d = 7.65    # eV
m_a = 16    # amu
m_b = 12    # amu
m_c = m_a   # amu
def accel(x_a, x_b, x_c):
    acc = [0,0,0]
    acc[0] = -2*d*a*(math.exp(-2*a*(x_b-x_a-b))-math.exp(-a*(x_b-x_a-b)))/m_a
    acc[2] = 2*d*a*(math.exp(-2*a*(x_c-x_b-b))-math.exp(-a*(x_c-x_b-b)))/m_c
    acc[1] = -(m_a*acc[0] + m_c*acc[2])/m_b
    return acc

print("Problem 1:________________________________________")
print("\nVelocity-Verlet Evolution Started...")
t = 0
dt = 0.05
N = 2048
pos = [[-b+0.025],[0.0],[b-0.025]]
v = [[0],[0],[0]]
time = [0]

while(t <= int(N*dt)):
    acc = accel(pos[0][int(t/dt)],pos[1][int(t/dt)],pos[2][int(t/dt)])
    acc_next = accel(pos[0][int(t/dt)] + v[0][int(t/dt)]*dt + acc[0]/2*dt**2, pos[1][int(t/dt)] + v[1][int(t/dt)]*dt + acc[1]/2*dt**2, pos[2][int(t/dt)] + v[2][int(t/dt)]*dt + acc[2]/2*dt**2)
    for i in range(3):
        pos[i].append(pos[i][int(t/dt)] + v[i][int(t/dt)]*dt + acc[i]/2*dt**2)
        v[i].append(v[i][int(t/dt)] + dt/2*(acc_next[i]+acc[i]))
    time.append(t)
    t += dt
print("Evolution Completed.")

dispBA = []
dispCB = []
for i in range(len(pos[0])):
    dispBA.append(pos[1][i]-pos[0][i])
    dispCB.append(pos[2][i]-pos[1][i])

pyplot.plot(time, v[0], label='Velocity of Right Oxygen Atom')
pyplot.legend()
pyplot.show()
pyplot.plot(time, dispBA, label='Right Oxygen-Carbon Displacement')
pyplot.legend()
pyplot.show()
pyplot.plot(time, dispCB, label='Left Oxygen-Carbon Displacement')
pyplot.legend()
pyplot.show()

# print("FFT Section Started...")
# numpy.v = v[0]
# print(len(v[0]))
# print(len(numpy.v))
# numpy.fTemp = numpy.fft.rfft(numpy.v)
# print(len(numpy.fTemp))
# fft = []
# n = []
# for i in range(N//2+1):
#     n.append(i)
#     fft.append(abs(numpy.fTemp[i]))

# print("Plotting FFT function...")
# pyplot.plot(n,fft,label='FFT of Right Oxygen Velocity Data')
# pyplot.legend()
# pyplot.show()


print("Problem 2:________________________________________")
print("\nVelocity-Verlet Evolution Started...")
t = 0
dt = 0.05
N = 2048
pos = [[-b-0.025*3/8],[0.0+0.025],[b-0.025*3/8]]
v = [[0],[0],[0]]
time = [0]

while(t <= int(N*dt)):
    acc = accel(pos[0][int(t/dt)],pos[1][int(t/dt)],pos[2][int(t/dt)])
    acc_next = accel(pos[0][int(t/dt)] + v[0][int(t/dt)]*dt + acc[0]/2*dt**2, pos[1][int(t/dt)] + v[1][int(t/dt)]*dt + acc[1]/2*dt**2, pos[2][int(t/dt)] + v[2][int(t/dt)]*dt + acc[2]/2*dt**2)
    for i in range(3):
        pos[i].append(pos[i][int(t/dt)] + v[i][int(t/dt)]*dt + acc[i]/2*dt**2)
        v[i].append(v[i][int(t/dt)] + dt/2*(acc_next[i]+acc[i]))
    time.append(t)
    t += dt
print("Evolution Completed.")

dispBA = []
dispCB = []
for i in range(len(pos[0])):
    dispBA.append(pos[1][i]-pos[0][i])
    dispCB.append(pos[2][i]-pos[1][i])

pyplot.plot(time, v[0], label='Velocity of Left Oxygen Atom')
pyplot.legend()
pyplot.show()
pyplot.plot(time, dispBA, label='Right Oxygen-Carbon Displacement')
pyplot.legend()
pyplot.show()
pyplot.plot(time, dispCB, label='Right Oxygen-Carbon Displacement')
pyplot.legend()
pyplot.show()