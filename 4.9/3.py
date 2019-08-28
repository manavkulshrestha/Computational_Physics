# Apply FTCS FD scheme to the heat equation.
# Here we solve for the temperature T(x,t) in a steel bar of lenght L
# with the intial temperature T(x,0) specified and the temperatures at
# the two ends of the bar T(0,t), T(L,t) fixed.
import numpy as np
import matplotlib.pyplot as plt

# Define physical system, initial and boundary conditions:
ll = 0.05  # size of space domain (m)
dd = 4.25e-6  # thermal diffusivity (m^2/s) (this is steel)
tt1 = 500.0  # left fixed-temp BC (deg C)
tt2 = 300.0  # right fixed-temp BC (deg C)
tt0 = 300.0  # initial temperature of the bar (deg C)

# Set the FTCS solution parameters:
nn = 100*2  # number of space points
#b) ^double this
xih = .50  # dimensionless time step, must be less than 1/2
#a) ^unstable for xih ~ 1
tplot = [1, 3, 10, 30, 100, 300]  # times at which to plot T(x) (s)

a = ll / (nn - 1)  # compute space step (m)
h = xih * a ** 2 / dd  # compute time step (s) to give specified xih
print('For xih = %.2f time step h = %.4f s' % (xih, h))
print('t_0 = ',ll**2/dd)
# Make array to hold solution and set up with
# initial and boundary conditions:
x = np.linspace(0, ll, nn)  # space points to use
tt = tt0 * np.ones(nn)  # make array for T(x), set to IC...
tt[0] = tt1
tt[-1] = tt2  # ...and to BC

hda = h * dd / a ** 2  # used in FD time step

def step(tt, hda):
    """Performs one time step, updating array tt."""
    tt[1:-1] += hda * (tt[:-2] + tt[2:] - 2 * tt[1:-1])

# Figure out time steps at which will plot solution:
jplot = []
for t in tplot:
    jplot.append(int(t / h + 0.5))

# Start the plot:
plt.rc('font', size=12)
plt.figure(figsize=(6, 4))
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$T$ ($^\circ$C)')

# Do the simulation:
for j in range(max(jplot) + 1):  # for each time step
    if j in jplot:  # if we are plotting at this time step..
        plt.plot(x, tt, label='t=%.1f s' % (j * h))  # ..add a curve to the plot
    step(tt, hda)  # do the FTCS step
plt.legend(fontsize=10)
plt.show()