"""make_galaxy2.py  3/7/19  D. Candela

Make 3D coordinates of stars in an imaginary galaxy then make 3D scatter plot
of the stars and optionally write star coordinates to a file.
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import cos,sin,arctan2,sqrt
from mpl_toolkits.mplot3d import Axes3D
from scipy import randn # gaussian-distributed random numbers

# Make 2D array of sprial disk star coordinates:
stars = 5000   # stars in disk
rr = 10.       # radius of disk, kpc
armn = 5       # number of spiral arms
armeps = 0.7   # arm density modulation strength, dimensionless
armtt = 3.0    # arm twist rate, dimensionless
x = rr*randn(stars)
y = rr*randn(stars)
z = np.zeros(stars)   # start with stars gaussian-distributed in xy plane
r = sqrt(x**2 + y**2)
thet = arctan2(y,x)   # convert to polar coordinates
thet2 = thet + (armeps/armn)*sin(armn*thet) +\
         armtt * r/rr  # add spiral arms by modifying theta
x2 = r*cos(thet2)
y2 = r*sin(thet2)   # convert back to cartesian
disk = np.stack((x2,y2,z),axis=1)  # stack x,y,z as columns of 2D array

# Make 2D array of bulge star coordinates:
starsb = int(stars/1.5) # stars in central bulge
rrb = rr/3.             # radius of cental bulge
xb = rrb*randn(starsb)
yb = rrb*randn(starsb)
zb = rrb*randn(starsb)               # make the bulge stars
bulge = np.stack((xb,yb,zb),axis=1)  # stack x,y,z as columns of 2D array

galaxy = np.concatenate((disk,bulge)) # combine disk and bulge to give galaxy


# Preliminaries to plotting:
xall = galaxy[:,0]
yall = galaxy[:,1]
zall = galaxy[:,2]   # slice into columns for x, y, z
nall = len(xall)     # how many stars

# Make the scatter plot:
plt.figure(figsize=(10,10))
plt.rc('font', size=12)
ax = plt.gca(projection="3d")         # get some 3D axes
ax.scatter(xall,yall,zall,s=1,c="m")  # do the scatter plot
psize = 25.0                      # size of plotting box
ax.set_xlim(-psize, psize)
ax.set_ylim(-psize, psize)
ax.set_zlim(-psize, psize)
ax.set_xlabel("x (kpc)")
ax.set_ylabel("y (kpc)")
ax.set_zlabel("z (kpc)")
plt.title ("Imaginary Galaxy with %d stars"%nall)
plt.show()

# Write the data to a file:
np.savetxt("galaxy2.txt",galaxy,newline="\r\n",fmt="%10.6f",
           header="%10s %10s %10s"%("x (kpc)","y (kpc)","z (kpc)"),
           comments="")