import numpy as np
import matplotlib.pyplot as plt

D = 50
points = 100

f_picture = np.zeros((points, points))
xy = np.linspace(-D, D, points)

x,y = np.meshgrid(xy,xy)
f_picture = np.sin((x**2 + y**2)**.5)

def density_plot(pic, title, x_label, y_label, figure_size=None):
    if figure_size is not None:
        plt.figure(figsize=figure_size)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.imshow(pic,origin='lower',extent=(-D,D,-D,D))
    plt.colorbar()
    plt.show()
    
density_plot(f_picture, 'Distance from origin', 'x-axis', 'y-axis', figure_size=(7,7))

f_picture = np.sin((x**2 + y**2)**.5 + np.arctan2(y, x))
f_picture2 = np.sin((x**2 + y**2)**.5 + 5*np.arctan2(y, x))
f_picture3 = np.sin((x**2 + y**2)**.5 + np.arctan2(y, x)/2)

density_plot(f_picture, '$sin{(r + \\theta)}$', 'x-axis', 'y-axis', figure_size=(7,7))
density_plot(f_picture2, '$sin{(r + 5\\theta)}$', 'x-axis', 'y-axis', figure_size=(7,7))
density_plot(f_picture3, '$sin{(r + \\theta/2)}$', 'x-axis', 'y-axis', figure_size=(7,7))