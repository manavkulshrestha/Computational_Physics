import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt,exp
from scipy.optimize import curve_fit

# Read the data from file
data = np.loadtxt('../cpresources/gl2.txt', float,skiprows=1) # read into 2D array
x = data[:,0]
y = data[:,1]

def fg(x,aa,x0,w,bb):
    """Model function: Gaussian plus linear background"""
    return aa*np.exp(-(x-x0)**2/(2*w**2)) + bb

# Use curve_fit to fit the data:
guesses = [1,1,1,1]   # parameter guesses
# guesses = [1 for i in range(6)]
(aa,x0,w,bb),cc = curve_fit(fg,x,y,p0=guesses)

# Print parameters and their 2-sigma uncertainties:
(uaa,ux0,uw,ubb) = 2*sqrt(np.diag(cc))
print('parameters and 2-sigma parameter uncertainties:')
print('A = %f +/- %f'%(aa,uaa))
print('x0 = %f +/- %f'%(x0,ux0))
print('w = %f +/- %f'%(w,uw))
print('w = %f +/- %f'%(bb,ubb))

# Compute reduced chi-squared:
yfit = fg(x,aa,x0,w,bb)
yys = (yfit-y)**2
dof = len(x) - len(guesses)    # degrees of freedom
chisqr = sum(yys)/dof
print()
print('Reduced chi-squared = %f'%chisqr)

# Plot data and model together
xmod = np.linspace(x[0],x[-1],100)       # assumes x's are in order
ymod = fg(xmod,aa,x0,w,bb)
plt.figure(figsize=(7.5,5))
plt.rc('font', size=16)
plt.plot(x,y,'bo') # plot the data
plt.plot(xmod,ymod,'r')                  # plot the model
plt.xlabel('x (cm)')
plt.ylabel('y (mV)')
plt.show()