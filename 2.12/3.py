import numpy as np
def atan(x, y):
    if x == 0:
        return np.pi/2
    elif x < 0 and y > 0:
        return -np.arctan(y/x) + np.pi
    elif x < 0 and y < 0:
        return -np.arctan(y/x) - np.pi
    return np.arctan(y/x)

def to_polar(x, y):
    return (x**2 + y**2)**.5, np.arctan(y/x) if x != 0 else '[div by 0]', atan(x, y), np.arctan2(y, x)

while True:
    x = float(input('x? '))
    y = float(input('y? '))

    r, theta_1, theta_2, theta_3 = to_polar(x, y)
    print(f'Original:\tr = {r}, theta = {theta_1}')
    print(f'Corrected:\tr = {r}, theta = {theta_3}')
    print(f'arctan2:\tr = {r}, theta = {theta_3}')
