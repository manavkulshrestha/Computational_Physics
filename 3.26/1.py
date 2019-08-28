import numpy as np
from numpy import sin, pi, linspace
import matplotlib.pyplot as plt
from scipy.integrate import odeint
R = 10 #ohms
C = 1e-3 #F
filt = 1/(R*C)

w = 50
def V_in(t):
    return 2*sin(w*t)

def model(y, x):
    return (V_in(x) - y)*filt

def f(y, t):
    return (t - y)*filt

def plot(x, ys, title, x_label, y_label, sub_plot=None):
    if sub_plot:
        plt.subplot(sub_plot)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    for y in ys:
        plt.plot(x, y)
        
t = linspace(0, 6*pi/w, 10)
V_outo50 = odeint(model, 0, t)
plot(t, (V_in(t), V_outo50), 'w = 50', 't', 'V_in & V_out (odeint)', sub_plot=221)

w = 300
t = linspace(0, 6*pi/w, 10)
V_outo300 = odeint(model, 0, t)
plot(t, (V_in(t), V_outo300), 'w =300', 't', 'V_in & V_out (odeint)', sub_plot=222)

len_t = len(t)

#Euler's method
V_oute300 = np.zeros(len_t);
i = 1
h = t[1]-t[0]
while i<len_t:
    V_oute300[i] = V_oute300[i-1] + h*(f(V_oute300[i-1], V_in(t[i-1])))
    i += 1
plot(t, (V_outo300, V_oute300), 'Euler\'s method', 't', 'V_out (odeint) & V_out (Euler\'s method)', sub_plot=223)

#RK2
V_outrk2300 = np.zeros(len_t)
i = 1
h = t[1]-t[0]
while i<len_t:
    V_outrk2300[i] = V_outrk2300[i-1] + h*f(V_outrk2300[i-1] + (h*f(V_outrk2300[i-1], V_in(t[i-1])))/2, V_in(t[i-1]) + h/2)
    i += 1
plot(t, (V_outo300, V_outrk2300, V_oute300), 'RK2', 't', 'odeint & RK2 & Euler\'s Method', sub_plot=224)

plt.show()

#RK4
V_out_rk4 = np.zeros(len_t)
i = 1
while i<len_t:
    k1 = h * f(V_out_rk4[i-1], V_in(t[i-1])) 
    k2 = h * f(V_out_rk4[i-1] + 0.5 * k1, V_in(t[i-1]) + 0.5 * h) 
    k3 = h * f(V_out_rk4[i-1] + 0.5 * k2, V_in(t[i-1]) + 0.5 * h) 
    k4 = h * f(V_out_rk4[i-1] + k3, V_in(t[i-1]) + h)
   
    V_out_rk4[i] = (V_out_rk4[i-1] + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4))
    i += 1

plt.plot(t,V_outo300,label='odeint')
plt.plot(t,V_outrk2300,label='RK2')
plt.plot(t,V_out_rk4,label='RK4')
plt.legend()
plt.show()