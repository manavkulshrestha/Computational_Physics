from scipy.integrate import dblquad
import numpy as np
from numpy import cos

for A,B in [(1,1),(1,2),(2,1),(30,30)]:
    print(dblquad(lambda y,x: y*cos(x*y),0,A,lambda x: 0,lambda x: B))
    print((1-cos(A*B))/A)
    print()