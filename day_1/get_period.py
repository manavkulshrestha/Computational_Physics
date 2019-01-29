from numpy import pi, sqrt, cos

g = 9.8 # acceleration of gravity (m/s**2)
L = float(input('L? '))
beta = float(input('Beta (in degrees)? ')) * pi/180
print(f'T = {2*pi*sqrt(L*cos(beta)/g)}')