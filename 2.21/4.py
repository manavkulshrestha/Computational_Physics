import numpy as np
import matplotlib.pyplot as plt
from numpy import cos
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

n = 100
r = 1

xlist = []
ylist = []
zlist = []

for theta in np.linspace(0,np.pi,n):
	for azim in np.linspace(0,2*np.pi,n):
		xlist.append(r * np.sin(theta) * np.cos(azim))
		ylist.append(r * np.sin(theta) * np.sin(azim))
		zlist.append(r * np.cos(theta))


plt.figure(figsize=(10,10))
plt.rc('font', size=12)
ax = plt.gca(projection='3d')
ax.scatter(xlist,ylist,zlist,s=1,c='m')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title ('Scatter Plot of Sphere')

plt.show()