import numpy as np
import numpy.linalg as la

A = np.array([[1,4,1],[4,-1,-1],[2,1,3]])
b = np.array([[-4],[3],[7]])

print('A = \n',A)
print('b = \n',b)

print('Using A^-1.\tx = \n',la.inv(A)@b)
print('Using rref.\tx = \n',la.solve(A,b))

x = la.solve(A,b)

# print(x[0]+4*x[1]+x[2])