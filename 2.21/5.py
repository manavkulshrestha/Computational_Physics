import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#determine order of polynomial
for terms in range(3, 4):
    guesses = [1 for i in range(terms)]

    data = np.loadtxt('../cpresources/w4bdata.txt', skiprows=1)
    x = data[:,0]
    y = data[:,1]
    yerr = data[:,2]
    nn = len(x)

    def f(x,*params):
        return sum(p*(x**i) for i,p in enumerate(params))

    params,cc = curve_fit(f,x,y,p0=guesses)
    print('Fit parameters:')
    for i,p in enumerate(params):
        print(f'p{i} = {p}')

    xmod = np.linspace(x[0],x[-1],100)
    ymod = f(xmod,*params)

    yfit = f(x,*params)

    plt.errorbar(x,y,yerr,fmt='bo',capsize=5)
    plt.xlabel('x (cm)')
    plt.ylabel('y (mV)')
    plt.plot(xmod,ymod,'r')
    plt.show()