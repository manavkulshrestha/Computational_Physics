import numpy as np

squares = np.array([[x, x*x] for x in range(20)])
np.savetxt("squares.csv", squares, delimiter=',', header='X,X^2', fmt='%.6f')