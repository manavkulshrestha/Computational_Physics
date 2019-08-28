import numpy as np

C = np.array([[1,3,2],[2,4,1],[5,6,5]])

print('C =\n',C)
print('C^-1 =\n',np.linalg.inv(C))

print('C^-1 . C =\n',np.linalg.inv(C)@C)