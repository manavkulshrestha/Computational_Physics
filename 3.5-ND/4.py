import numpy as np

A = np.array([[1,3],[2,4],[5,6]])
B = np.array([[2,1,4],[3,2,1]])


print(f'A . B = \n{A@B}')
# (A.B)[1,1] = 1*1 + 3*3 = 11
print('(A.B)[1,1] = 11')

print(f'B . A = \n{B@A}')
# (B.A)[1,1] = 1*2 + 2*1 + 4*5 = 24
print('(B.A)[1,1] = 24')