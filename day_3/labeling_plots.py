import numpy as np
import matplotlib.pyplot as plt
from numpy import pi,sin,cos

x = np.linspace(0,10,100)
f1 = sin(x)
g1 = cos(x)

plt.plot(x,f1,'c--', label='sin(x)')
plt.plot(x,g1,'m--', label='cos(x)')
plt.ylim(bottom=-2, top=3)

plt.title('Elaborate Plots',fontsize=20)
plt.xlabel('X axis')
plt.ylabel('sin(x) and cos(x)')
plt.legend(fontsize=12)

plt.show()