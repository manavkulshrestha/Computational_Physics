import numpy as np
from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 1
b = .5
g = .5
d = 2

def model(RF,t):
	R,F = RF

	dRdt = a*R - b*R*F
	dFdt = g*R*F - d*F

	return dRdt, dFdt

t = linspace(0, 15, 100)

R_0 = 2
F_0 = 2
RF = odeint(model, (R_0, F_0), t)

plt.plot(t,RF[:,0],label='R') # plot first column of solution which is x(t)
plt.plot(t,RF[:,1],label='F') # plot first column of solution which is y(t)
plt.xlabel('t')
plt.ylabel('R or F')
plt.legend()
plt.show()