import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def N(t, N_0, r, B):
    return N_0*np.exp(-t/r) + B

def N2(t, N_0, r):
    return N_0*np.exp(-t/r) + 25

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

guesses = [[200,250,0],[1,1,1]]

for i in range(2):
    params,cc = curve_fit(N,data[i][:,0],data[i][:,1],p0=guesses[i])

    xmod = np.linspace(data[i][:,0][0],data[i][:,0][-1],100)
    print('fitting params = ',params)
    print('cc = ',cc)
    ymod = N(xmod, *params)

    plot_ens(data[i][:,0], data[i][:,1], np.sqrt(data[i][:,1]), 'Radioactive decay', 't (mins)', 'count (/min)', subplots=[1,2, i+1], y_scale='log')
    plt.plot(xmod, ymod, 'r')

plt.show()

guesses = [[200,250],[1,1]]

for i in range(2):
    params,cc = curve_fit(N2,data[i][:,0],data[i][:,1],p0=guesses[i])

    xmod = np.linspace(data[i][:,0][0],data[i][:,0][-1],100)
    print('fitting params = ',params)
    ymod = N2(xmod, *params)

    plot_ens(data[i][:,0], data[i][:,1], np.sqrt(data[i][:,1]), 'Radioactive decay', 't (mins)', 'count (/min)', subplots=[1,2, i+1], y_scale='log')
    plt.plot(xmod, ymod, 'r')

plt.show()