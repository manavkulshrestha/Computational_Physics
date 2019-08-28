from scipy.integrate import quad
from numpy import linspace,sin,cos
import numpy as np
import matplotlib.pyplot as plt

def f(u):
	return u*sin(u)

def exact(x):
    return sin(x) - x*cos(x)

def trap(f,x,N):
    ls = linspace(0,x,N)
    coeff = np.full(N,1)
    coeff[0] = .5
    coeff[-1] = .5
    
    return (x/N) * np.sum(coeff*f(ls))

def simps(f,x,N):
    return trap(f,x,N+(N&1))

def plot(x,ys,title,x_label,y_label,x_lim=None,y_lim=None,label_=None):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if isinstance(ys,tuple):
        for y in ys:
            plt.plot(x,y,label=label_)
    else:
        plt.plot(x,ys,label=label_)
    if x_lim:
        plt.xlim(*x_lim)
    if y_lim:        
        plt.ylim(*y_lim)
        
x = linspace(0,20,1000)
N = int(input('N? '))

y_exact = exact(x)

y_simps = [simps(f,point,N)+5 for point in x]
y_quad = [quad(f,0,point)[0]+10 for point in x]

plot(x,y_exact,'','x','$x sin(x^2)$',label_='Trapezoid')
plot(x,y_simps,'','x','$x sin(x^2)$',label_='Simpon\'s rule')
plot(x,y_quad,'','x','$x sin(x^2)$',label_='Exact')

#plt.show()
