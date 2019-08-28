import numpy as np
import matplotlib.pyplot as plt

def N(N_0, t, r, B):
    return N_0*np.exp(-t/r) + B

def plot_ens(x, y, yerr, title, x_label, y_label, subplots=None, y_scale=None):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if subplots is not None:
        plt.subplot(*subplots)
    if y_scale is not None:
        plt.yscale('log')
    plt.errorbar(x,y,yerr,fmt='co',capsize=5)

data = [np.loadtxt(f'../cpresources/decay{i}.txt', float, skiprows=1) for i in range(1,3)]

plt.figure()

for i in range(2):
    plot_ens(data[i][:,0], data[i][:,1], np.sqrt(data[i][:,1]), 'Radioactive decay', 't (mins)', 'count (/min)', subplots=[1,2, i+1], y_scale='log')

plt.show()