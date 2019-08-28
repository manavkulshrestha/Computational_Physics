import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt,exp
from scipy.optimize import curve_fit

# Read the data from file
data = np.loadtxt('../cpresources/peak4.txt', float,skiprows=1) # read into 2D array
x = data[:,0]
y = data[:,1]

def f(x,aa,x0,w,bb0,bb1,bb2):
    """Model function: Gaussian plus linear background"""
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x + bb2*(x**2)

# Use curve_fit to fit the data:
guesses = [3,5,1,1,0,0]   # parameter guesses
# guesses = [1 for i in range(6)]
(aa,x0,w,bb0,bb1,bb2),cc = curve_fit(f,x,y,p0=guesses)

# Print parameters and their 2-sigma uncertainties:
(uaa,ux0,uw,ubb0,ubb1,ubb2) = 2*sqrt(np.diag(cc))
print('parameters and 2-sigma parameter uncertainties:')
print('A = %f +/- %f'%(aa,uaa))
print('x0 = %f +/- %f'%(x0,ux0))
print('w = %f +/- %f'%(w,uw))
print('B0 = %f +/- %f'%(bb0,ubb0))
print('B1 = %f +/- %f'%(bb1,ubb1))
print('B2 = %f +/- %f'%(bb2,ubb2))

# Compute reduced chi-squared:
yfit = f(x,aa,x0,w,bb0,bb1,bb2)
yys = (yfit-y)**2
dof = len(x) - len(guesses)    # degrees of freedom
chisqr = sum(yys)/dof
print()
print('Reduced chi-squared = %f'%chisqr)

# Plot data and model together
xmod = np.linspace(x[0],x[-1],100)       # assumes x's are in order
ymod = f(xmod,aa,x0,w,bb0,bb1,bb2)
plt.figure(figsize=(7.5,5))
plt.rc('font', size=16)
plt.plot(x,y,'bo') # plot the data
plt.plot(xmod,ymod,'r')                  # plot the model
plt.show()