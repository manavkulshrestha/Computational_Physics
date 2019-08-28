import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt,exp
from scipy.optimize import curve_fit

def fl(x,aa,x0,w,bb):
    """Model function: Lorentzian"""
    return (aa)/(1 + ((x-x0)/w)**2) + bb

data = np.loadtxt(f'../cpresources/gl1.txt', float,skiprows=1) # read into 2D array
x = data[:,0]
y = data[:,1]

# Use curve_fit to fit the data:
guesses = [2,-2,5,-1]   # parameter guesses
(aa,x0,w,bb),cc = curve_fit(fl,x,y,p0=guesses)

# Print parameters and their 2-sigma uncertainties:
(uaa,ux0,uw,ubb) = 2*sqrt(np.diag(cc))
print('parameters and 2-sigma parameter uncertainties:')
print('A = %f +/- %f'%(aa,uaa))
print('x0 = %f +/- %f'%(x0,ux0))
print('w = %f +/- %f'%(w,uw))
print('w = %f +/- %f'%(bb,ubb))

# Compute reduced chi-squared:
yfit = fl(x,aa,x0,w,bb)
yys = (yfit-y)**2
dof = len(x) - len(guesses)    # degrees of freedom
chisqr = sum(yys)/dof
print()
print('Reduced chi-squared = %f'%chisqr)

# Plot data and model together
xmod = np.linspace(x[0],x[-1],100)       # assumes x's are in order
ymod = fl(xmod,aa,x0,w,bb)
plt.figure(figsize=(7.5,5))
plt.rc('font', size=16)
plt.plot(x,y,'bo') # plot the data
plt.plot(xmod,ymod,'r')                  # plot the model
plt.show()