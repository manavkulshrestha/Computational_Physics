import numpy as np
import matplotlib.pyplot as plt
from numpy import cos
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def wave(x, y):
	r = np.sqrt(x**2 + y**2);
	return x*(6-r)*np.exp(-r/3)

xy = np.linspace(-20, 20, 100)

x,y = np.meshgrid(xy, xy)
z = wave(x, y)

def density_plot(data, title, x_label, y_label):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.imshow(data)
    plt.colorbar()
    
density_plot(z, 'Suface Plot of $\psi(x, y)$', 'x-axis', 'y-axis')
plt.show()