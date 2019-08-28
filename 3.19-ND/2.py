# import sys
# print(sys.executable)

from scipy.integrate import quad
from numpy import cos,sin

def f(x):
	return x*sin(x**2)

print('using worked out integral: ',(cos(1)-cos(25))/2)
print('using scipy.integrate',quad(f,1,5)[0]);
