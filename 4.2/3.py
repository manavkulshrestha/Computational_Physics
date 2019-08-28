from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

M = 2e30
G = 6.8e-11

def model(xvxyvy, t):
    x,vx,y,vy = xvxyvy

    dxdt = vx
    dydt = vy

    const = -G * M / ((x ** 2 + y ** 2) ** (3 / 2))

    dvxdt = const*x
    dvydt = const*y

    return dxdt, dvxdt, dydt, dvydt

x_0 = 0
y_0 = 1.5e10
vx_0 = 3e4
vy_0 = 0

t_max = 3.2e7
t_max = 4e5
t = linspace(0, t_max, 100)

l = 1.5e10

xvxyvy = odeint(model, (x_0, vx_0, y_0, vy_0), t)

plt.subplot(221)
plt.title('x(t)')
plt.plot(t,xvxyvy[:,0])
plt.xlabel('t (s)')
plt.ylabel('y (m)')

plt.subplot(222)
plt.title('y(t)')
plt.plot(t,xvxyvy[:,2])
plt.xlabel('t (s)')
plt.ylabel('y (m)')

plt.subplot(223)
plt.xlim(-l,l)
plt.ylim(-l,l)
plt.title('y(t)')
plt.plot(xvxyvy[:,0],xvxyvy[:,2])
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()