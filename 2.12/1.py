import matplotlib.pyplot as plt
import numpy as np

xs = [np.linspace(0,10,100) for i in range(4)]
fs = [np.cos(xs[0]), np.sin(xs[1]), 3*(xs[2]), np.tan(xs[3])]

plt.figure()

plt.subplot(2,2,1)
plt.plot(xs[0], fs[0], 'g--')

plt.subplot(2,2,2)
plt.plot(xs[1], fs[1], 'g--')

plt.subplot(2,2,3)
plt.plot(xs[2], fs[2], 'g--')

plt.subplot(2,2,4)
plt.plot(xs[3], fs[3], 'g--')
plt.show()