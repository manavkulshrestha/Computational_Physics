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

def simps(f,a,b,N):
    add = N&1
    N += add
    if add == 1:
        print(f'Changed N to be {N}')
    
    return trap(f,a,b,N)

while True:
    N = int(input('N? '))
    if N < 1:
        break;
        
    print(f'\nWith {N} slices: {trap(f,lower,upper,N):.6f}\n')    
    print(f'Simpsons\' rule: {simps(f,lower,upper,N)}\n')
    print('Exact: ',quad(f,1,5)[0]);