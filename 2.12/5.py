import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000)

def func(x):
    return x + 2*np.cos(x**2)

def func_abs(x):
    return abs(x) + 2*np.cos(x**2)

def plot_noshow(x, y, title, x_label, y_label):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y)
    
plot_noshow(x, func(x), 'Graph for $x + 2cos{x^2}$', 'x', '$f(x) = x + 2cos{x^2}$')
plot_noshow(x, func(x)+10, 'Graph for $x + 2cos{x^2} + 10$', 'x', '$f(x) = x + 2cos{x^2}$')
plot_noshow(x, func(x+5), 'Graph for $x + 2cos{(x)^2}$', 'x', '$f(x) = x + 2cos{x^2}$')

plt.show()

plot_noshow(x, func_abs(x), 'Graph for $x + 2cos{|x|^2}$', 'x', '$f(x) = x + 2cos{x^2}$')
plot_noshow(x, func_abs(x)+10, 'Graph for $x + 2cos{|x|^2} + 10$', 'x', '$f(x) = x + 2cos{x^2}$')
plot_noshow(x, func_abs(x+5), 'Graph for $x + 2cos{|x|^2}$', 'x', '$f(x) = x + 2cos{x^2}$')

plt.show()