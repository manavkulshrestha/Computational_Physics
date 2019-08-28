from numpy.random import randint
import numpy as np

W = 50
S = 100

walk = np.empty(S)
walk[0] = 0

t = list(range(S))

for walker in range(W):
    for step in range(1,S):
        walk[step] = walk[step-1]+(-1)**randint(1,3)
    plt.plot(t,walk)
    
plt.show()