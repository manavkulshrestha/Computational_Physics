import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)

def func(x):
    return np.cos(x)**2 + 5

def hist(x, y, title, x_label, y_label):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.hist(y)
    plt.show()

def plot(x, y, title, x_label, y_label):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y)
    plt.show()
    
plot(x, func(x), 'Graph for $x + 2cos{x^2}$', 'x', '$f(x) = x + 2cos{x^2}$')
hist(x, func(x), 'Hist for $x + 2cos{x^2}$', 'x', '$f(x) = x + 2cos{x^2}$')

plt.show()