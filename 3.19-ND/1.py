import numpy as np
from numpy import linspace

print(f'3+4i / 5+6i = {(3+4j)/(5+6j)}')
#(3+4i)/(5+6i) = (3*5 + 4*6)/(25 + 36) + i(4*5 - 3*6)/(25 + 36) = 39/61 + i(2/61) = 0.63934426229+i0.03278688524

print(f'exp(2j) = {np.exp(2j)}')
#e^(2i) = cos(2) + isin(2) -0.416146837+i0.909297427

print(f'cos(3j) = {np.cos(3j)}')
# e^3 = 20.0855369
# cos(3i) = (e^i*3i + e^-i*3i)/2 = (e^-3 + e^3)/2 = (1/20.0855369 + 20.0855369)/2 = 10.0676619842

z = 5+0.2j
t = linspace(1,10,100)

def f(t):
    return exp(complex(0,z*t))

real = cos(z*t)
imag = sin(z*t)

def plot_noshow(x, y, title, x_label, y_label, subplot=None, figsize=None, hspace=None, wspace=None):
    if subplot is not None:
        plt.subplot(*subplot)
    if figsize is not None:
        plt.figure(figsize=figsize)
    if wspace is not None:
        plt.subplots_adjust(wspace=wspace)
    if hspace is not None:
        plt.subplots_adjust(hspace=hspace)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y)

def plot(x, y, title, x_label, y_label, subplot=None, figsize=None, hspace=None, wspace=None):
    plot_noshow(x, y, title, x_label, y_label, subplot=subplot, figsize=figsize, hspace=hspace, wspace=wspace)
    plt.show()
    
plot_noshow(t,real,'t vs Real','t','Real',subplot=[2,2,1])
plot_noshow(t,imag,'t vs Imag','t','Imag',subplot=[2,2,3])
plot_noshow(real,imag,'Real vs Imag','Real','Imag',subplot=[1,2,2])

plt.show()