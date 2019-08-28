import numpy as np
import matplotlib.pyplot as plt
from numpy import cos
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def wave(x, y):
	r = np.sqrt(x**2 + y**2);
	return x*(6-r)*np.exp(-r/3)

a_0 = 5.29 * 10**-11

xy = np.linspace(-20, 20, 100)

x,y = np.meshgrid(xy, xy)
z = wave(x, y)

# make the surface plot
plt.figure(figsize=(12,8))
plt.rc('font', size=12)
ax = plt.gca(projection='3d')          # get some 3D axes
ax.plot_surface(x,y,z,cmap=cm.plasma, rcount=300, ccount=300)  # do the surface plot
ax.set_zlim(-4, 4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title ('Suface Plot of $\psi(x, y)$')

plt.show()