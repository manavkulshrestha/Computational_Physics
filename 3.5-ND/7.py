import numpy as np
from numpy import pi, cos, sin, linspace, transpose
import numpy.linalg as la

rotmats = [np.array([[cos(theta), -sin(theta)],[sin(theta), cos(theta)]]) for theta in [pi/4, pi/2, 3*pi/2]]

for R in rotmats:
	print('R^T = \n',transpose(R))
	print('R = \n',R)
	print('R^T . R = \n',transpose(R)@R)


print()

r = np.array([[1],[0]])
for R in rotmats:
	print('R . r = \n',R@r);

# expected [cos(pi/4), sin(PI/4)], [0,1], [0,1]