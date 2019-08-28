import numpy as np
from numpy.random import standard_cauchy as cauchy

S = 1
lim = 10
plt.hist([sum(cauchy() for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
plt.show()

lim = 1000
S = 100
plt.hist([sum(cauchy() for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,50))
plt.show()