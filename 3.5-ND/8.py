from numpy.random import randn
from numpy import cos,sin,pi
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

xy = np.array([[randn() for i in range(10)] for j in range(2)])
# x = randn(10)
# y = randn(10)
print(xy)

def rot(theta):
	return np.array([[cos(theta), -sin(theta)],[sin(theta), cos(theta)]])

plt.plot(xy[0,:],xy[1,:],'o',label='no rotation')

r = rot(pi/2)
for i in range(10):
	xyir = r@xy[:,i]
	plt.plot(xyir[0],xyir[1],'ro',label = None if i != 1 else 'rotation by pi/2')

r = rot(.1)
for i in range(10):
	xyir = r@xy[:,i]
	plt.plot(xyir[0],xyir[1],'go',label=None if i != 1 else 'rotation by .1')

plt.legend()
plt.show()