import numpy as np
import matplotlib.pyplot as plt
from numpy import pi,sin,cos

x = np.linspace(0,10,200)
f1 = sin(x)
g1 = np.exp(x)

plt.clf()
plt.plot(x,f1,'g--')
plt.show()

plt.clf()
plt.plot(x,g1,'r--')
plt.show()

plt.clf()
plt.plot(x,f1,'g--')
plt.plot(x,g1,'r--')
plt.ylim(bottom=-2, top=3)

plt.show()
