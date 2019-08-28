import numpy as np
from numpy import pi,sin,cos,exp,real,imag
from scipy.fftpack import fft, dct
import matplotlib.pyplot as plt


def f(t):
	v1 = 20e3 # Hz
	v2 = 25e3 # Hz
	return sin(2*pi*v1*t) + cos(2*pi*v2*t)


tau = 2e-6
nn = 1000
t = np.linspace(0, nn*tau, nn)
f = f(t)

plt.subplot(1, 2, 1)
plt.rc('font',size=12)
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$f(t)$')
plt.plot(t,f)

plt.subplot(1, 2, 2)
dnu = 1/(2*nn*tau)  # frequency spacing in Hz
nu = np.linspace(0,(nn-1)*dnu,nn) # array of frequencies (Hz)
ftwid = dct(f) # do the discrete FT
plt.plot(nu/1e3,real(ftwid),label=r'[$\tilde{f}(\nu)$]')
plt.legend()
plt.xlabel(r'$\nu$ (kHz)')
plt.show()