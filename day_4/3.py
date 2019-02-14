import numpy as np
def atan(x, y):
    # if(x > 0):
    #     return np.arctan(y/x)
    # elif(x == 0):
    #     if(y == 0):
    #         return None
    #     return np.pi*(-1 if y<0 else 1)
    # return np.arctan(y/x) + np.pi*(-1 if y<0 else 1) # x < 0
    if(y == 0):
        if(x == 0):
            return None
        elif(x < 0):
            return np.pi
    if(x > 0):
        return 2*np.arctan(y/((x**2 + y**2)**.5 + x))
    return None
        


def to_polar(x, y):
    return (x**2 + y**2)**.5, np.arctan(y/x), atan(x, y), np.arctan2(x, y)

while True:
    x = float(input('x? '))
    y = float(input('y? '))

    if(x == 0):
        print("can\'t divide by 0")
        continue

    r, theta_1, theta_2, theta_3 = to_polar(x, y)
    print(f'Original:\tr = {r}, theta = {theta_1}')
    print(f'Corrected:\tr = {r}, theta = {theta_2}')
    print(f'arctan2:\tr = {r}, theta = {theta_3}')
