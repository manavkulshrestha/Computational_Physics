import numpy as np

def to_polar(x, y):
    return (x**2 + y**2)**.5, np.arctan(y/x)

while True:
    r, theta = to_polar(float(input('x? ')), float(input('y? ')))
    print (f'r = {r}, theta = {theta}')