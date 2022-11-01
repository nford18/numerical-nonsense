import math
import matplotlib.pyplot as pyplot
import scipy.fft

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
print("Velocity-Verlet Evolution Started...")
t = 0
dt = 0.05
N = 2**10
pos = [[-b+0.025],[0.0],[b-0.025]]
v = [[0],[0],[0]]
time = [0]

while(t <= N):
    acc = accel(pos[0][t],pos[1][t],pos[2][t])
    acc_next = accel(pos[0][t] + v[0][t]*dt + acc[0]/2*dt**2, pos[1][t] + v[1][t]*dt + acc[1]/2*dt**2, pos[2][t] + v[2][t]*dt + acc[2]/2*dt**2)
    for i in range(3):
        pos[i].append(pos[i][t] + v[i][t]*dt + acc[i]/2*dt**2)
        v[i].append(v[i][t] + dt/2*(acc_next[i]+acc[i]))
    time.append(t*dt)
    t += 1
print("Evolution Completed.")

dispBA = []
dispCB = []
for i in range(len(pos[0])):
    dispBA.append(pos[1][i]-pos[0][i])
    dispCB.append(pos[2][i]-pos[1][i])

print("\nGraphing Symmetric Molecule Vibration")
pyplot.plot(time, v[0], label='Velocity of Right Oxygen Atom')
pyplot.legend()
pyplot.show()
pyplot.plot(dispCB, dispBA, label='Right Oxygen-Carbon Displacement vs\nLeft Oxygen-Carbon Displacement')
pyplot.legend()
pyplot.show()

print("\nFFT Section Started...")
fftTemp = scipy.fft.rfft(v[0])
fft = []
n = []
for i in range(N//2-2):
    n.append(i)
    fft.append(abs(fftTemp[i]))

print("Plotting FFT function...")
print("Dominant Frequency found at n=20: f =", round(20/N/dt,5), "\be14 Hz")
print("Dominant Angular Frequency:\t  \u03C9 =", round(2*math.pi*20/N/dt,5), "\be14 rad/s")
pyplot.plot(n,fft,label='FFT of Left Oxygen Velocity Data')
# pyplot.xlim(15,25)
pyplot.legend()
pyplot.show()


print("\n\nProblem 2:________________________________________")
print("Velocity-Verlet Evolution Started...")
t = 0
dt = 0.05
N = 2**10
pos = [[-b-0.025*3/8],[0.0+0.025],[b-0.025*3/8]]
v = [[0],[0],[0]]
time = [0]

while(t <= N):
    acc = accel(pos[0][t],pos[1][t],pos[2][t])
    acc_next = accel(pos[0][t] + v[0][t]*dt + acc[0]/2*dt**2, pos[1][t] + v[1][t]*dt + acc[1]/2*dt**2, pos[2][t] + v[2][t]*dt + acc[2]/2*dt**2)
    for i in range(3):
        pos[i].append(pos[i][t] + v[i][t]*dt + acc[i]/2*dt**2)
        v[i].append(v[i][t] + dt/2*(acc_next[i]+acc[i]))
    time.append(t*dt)
    t += 1
print("Evolution Completed.")

dispBA = []
dispCB = []
for i in range(len(pos[0])):
    dispBA.append(pos[1][i]-pos[0][i])
    dispCB.append(pos[2][i]-pos[1][i])

print("\nGraphing Asymmetric Molecule Vibration")
pyplot.plot(time, v[0], label='Velocity of Left Oxygen Atom')
pyplot.legend()
pyplot.show()
pyplot.plot(dispCB, dispBA, label='Right Oxygen-Carbon Displacement vs\nLeft Oxygen-Carbon Displacement')
pyplot.legend()
pyplot.show()

print("\nFFT Section Started...")
fftTemp = scipy.fft.rfft(v[0])
fft = []
n = []
for i in range(N//2-2):
    n.append(i)
    fft.append(abs(fftTemp[i]))

print("Plotting FFT function...")
print("Dominant Frequency found at n=38: f =", round(38/N/dt,5), "\be14 Hz")
print("Dominant Angular Frequency:\t  \u03C9 =", round(2*math.pi*38/N/dt, 5), "\be14 rad/s")
pyplot.plot(n,fft,label='FFT of Left Oxygen Velocity Data')
# pyplot.xlim(25,45)
pyplot.legend()
pyplot.show()

print("\nFile Executed.")