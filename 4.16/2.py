import numpy as np
import matplotlib.pyplot as plt

# Define physical system, initial and boundary conditions:
ll = 1e-3                      # size of space domain (m)
dd = 1.6e-9                  # thermal diffusivity (m^2/s) (water)
x0 = 250e-6
cc0 = 10.0                    # initial temperature of the bar (ppm)
    
# Set the FTCS solution parameters:
nn = 200                      # number of space points
xih = 0.4                     # dimensionless time step, must be less than 1/2
tplot=[0, 10, 30, 100, 300, 1000]  # times at which to plot C(x) (s)

a = ll/(nn-1)              # compute space step (m)
h = (xih*a**2/dd)          # compute time step (s) to give specified xih
print('For xih = %.2f time step h = %.4f s'%(xih,h))

# Make array to hold solution and set up with
# initial and boundary conditions:
x = np.linspace(0, ll, nn)  # space points to use
cc = np.empty(nn)           # make array for C(x), set to IC...
nx0left = (nn/2) - nn*(x0/ll)
nx0right = (nn/2) + nn*(x0/ll)

for i in range(0, nn):
    if i > nx0left and i < nx0right:
        cc[i] = cc0
        
hda = h*dd/a**2           # used in FD time step


def step(cc, hda):
    """Performs one time step, updating array cc."""
    cc[1:-1] += hda*(cc[:-2] + cc[2:] - 2*cc[1:-1])
    cc[0] = cc[1]
    cc[-1] = cc[-2]


# Figure out time steps at which will plot solution:
jplot=[]
for t in tplot:
    jplot.append(int(t/h+0.5))

# Start the plot:
plt.rc('font',size=12)
plt.figure(figsize=(6,4))
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$T$ ($^\circ$C)')

# Do the simulation:
for j in range(max(jplot)+1):  # for each time step
    if j in jplot:             # if we are plotting at this time step..
        plt.plot(x,cc,label='t=%.1f s'%(j*h)) # ..add a curve to the plot
    step(cc,hda)               # do the FTCS step
plt.legend(fontsize=10)
plt.show()