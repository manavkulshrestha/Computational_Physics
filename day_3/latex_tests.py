import numpy as np
import matplotlib.pyplot as plt
from numpy import pi,sin,cos

x = np.linspace(0,10,100)
f1 = -x**3+1.5
g1 = cos(x)

plt.plot(x,f1,'c--', label='$-x^2 + \\frac{3}{2}$')
plt.plot(x,g1,'m--', label='cos(x)')
plt.ylim(bottom=-2, top=3)

plt.title('Dotted plots',fontsize=20)
plt.xlabel('X axis')
plt.ylabel('$-x^2 + \\frac{3}{2}$ and $cos(x)$')
plt.legend(fontsize=12)

plt.show()