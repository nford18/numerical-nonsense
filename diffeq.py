#################################################
#     Numerical Approximations for ODE Sols.    #
#################################################

def rungeKutta_2(t_0, t_final, t_step, x_init, deriv):
    t = t_0
    dt = t_step
    N = int(t_final/dt)
    x = x_init
    pos_x = []
    time = []

    while(t <= N):
        k1 = deriv(t,x)
        k2 = deriv(t+dt, x+k1*dt)
        x += (k1+k2)*dt/2
        t += dt
        pos_x.append(x)
        time.append(t)
    return [time, pos_x]



# 𝑘1 = 𝑓(𝑡𝑛, 𝑥𝑛)
# 𝑘2 = 𝑓(𝑡𝑛 + ∆𝑡, 𝑥𝑛 + 𝑘1(∆𝑡)) = 𝑓(𝑡𝑛 + ∆𝑡, 𝑥𝑛 + (∆𝑡)𝑓(𝑡𝑛, 𝑥𝑛))
# 𝑥𝑛+1 = 𝑥𝑛 + (∆𝑡)(𝑘1 + 𝑘2)/2, 𝑛 = 0, 1,2, …