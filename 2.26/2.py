import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

order_and_chi = []

#determine order of polynomial
for terms in range(2,10):
    guesses = [1 for i in range(terms)]

    data = np.loadtxt('../cpresources/data3.txt', skiprows=1)
    x = data[:,0]
    y = data[:,1]
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
    yys = (yfit-y)**2
    dof = len(x) - len(guesses)
    chisqr = sum(yys)/dof
    order_and_chi.append((terms-1, chisqr))
    print(f'Reduced chi-squared = {chisqr}')

    plt.errorbar(x,y,fmt='bo',capsize=5)
    plt.plot(xmod,ymod,'r')
    plt.show()

print(order_and_chi)