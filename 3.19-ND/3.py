from scipy.integrate import quad
from numpy import linspace
import numpy as np

def f(x):
	return x*sin(x**2)

lower = 1
upper = 5

def trap(f,a,b,N):
    ls = linspace(a,b,N)
    coeff = np.full(N,1)
    coeff[0] = .5
    coeff[-1] = .5
    
    return ((b-a)/N) * np.sum(coeff*f(ls))
    
while True:
    N = int(input('N? '))
    if N < 1:
        break;
        
    print(f'With {N} slices: {trap(f,lower,upper,N):.6f}')    
    print('Exact: ',quad(f,1,5)[0]);
        