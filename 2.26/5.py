import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# guesses = [1 for i in range(2)]
guesses = [1,40,1,1]

data = np.loadtxt('../cpresources/wavedata.txt', skiprows=1)
x = data[:,0]
y = data[:,1]
nn = len(x)

def f(x,*params):
    return params[0] + params[1]*np.sin(params[2]*x+params[3])

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
print(f'Reduced chi-squared = {chisqr}')

plt.errorbar(x,y,fmt='bo',capsize=5)
plt.plot(xmod,ymod,'r')
plt.show()