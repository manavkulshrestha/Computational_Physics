import numpy as np
from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 1
k = 1
x_0 = 0
v_0 = 1

def model1(xv, t):
    x,v = xv
    dxdt = v
    dvdt = -k * x * (1 + (x/100)**10)/m

    return dxdt, dvdt

def model2(xv, t):
    x,v = xv
    dxdt = v
    dvdt = -k * x * (1 + (x/.01)**10)/m

    return dxdt, dvdt

t = linspace(0, 10, 100)

xvodeint = odeint(model1, (x_0, v_0), t)
plt.subplot(121)
plt.plot(t,xvodeint[:,0])
plt.xlabel('x')
plt.ylabel('t')

xvodeint = odeint(model2, (x_0, v_0), t)
plt.subplot(122)
plt.plot(t,xvodeint[:,0])
plt.xlabel('x')
plt.ylabel('t')
plt.show()