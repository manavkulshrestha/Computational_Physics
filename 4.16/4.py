import numpy as np
from numpy import pi,sin,cos,exp,real,imag
from numpy.random import rand, randn
from scipy.fftpack import fft, dct, idct
import matplotlib.pyplot as plt


def f(t):
    v1 = 20e3 # Hz
    v2 = 25e3 # Hz
    return sin(2*pi*v1*t) + cos(2*pi*v2*t)


tau = 2e-6
nn = 1000
t = np.linspace(0, nn*tau/10000, nn)
f = f(t)
f2 = f + 0.7*randn(nn)

plt.figure(figsize=(17, 7))

plt.subplot(2, 2, 1)
plt.rc('font',size=12)
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$f(t)$')
plt.plot(t, f2)

plt.subplot(2, 2, 2)
dnu = 1/(nn*tau)  # frequency spacing in Hz
nu = np.linspace(0, (nn-1)*dnu, nn)  # array of frequencies (Hz)
ftwid = dct(f2)
plt.plot(nu/1e3, real(ftwid),label=r'[$\tilde{f}(\nu)$]')
plt.xlabel(r'$\nu$ (kHz)')

plt.subplot(2, 2, 3)
vmin = 200
for i, e in enumerate(ftwid):
    if e < vmin:
        ftwid[i] = 0
plt.plot(nu/1e3, real(ftwid), label=r'[$\tilde{f}(\nu)$]')
plt.xlabel(r'$\nu$ (kHz)')

plt.subplot(2, 2, 4)
inversed = idct(ftwid)
plt.plot(nu/1e3, real(inversed), label=r'[$\tilde{f}(\nu)$]')
plt.xlabel(r'$\nu$ (kHz)')

plt.show()