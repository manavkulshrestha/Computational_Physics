from numpy import pi,cross,linspace
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg as la

def rmat(n,theta,nhat):
    """Returns 3D rotation matrix thru theta(rad) about unit vector nhat"""
    return la.expm(np.cross(np.eye(n),nhat*theta))

v1 = np.array([0,0,2])
v2 = np.array([3,0,0])

print(f'v1 = {v1}\nv2 = {v2}\n')

rotation = np.array([1,0,0])
rotation = rmat(3,pi/2,rotation/la.norm(rotation))
print(f'rotation of pi/2 about x = \n{rotation}')
print(f'applied to v1 = {rotation@v1}')
print(f'applied to v2 = {rotation@v2}\n')

rotation = np.array([0,1,0])
rotation = rmat(3,pi/2,rotation/la.norm(rotation))
print(f'rotation of pi/2 about x = \n{rotation}')
print(f'applied to v1 = {rotation@v1}')
print(f'applied to v2 = {rotation@v2}\n')

rotation = np.array([0,0,1])
rotation = rmat(3,pi/2,rotation/la.norm(rotation))
print(f'rotation of pi/2 about z = \n{rotation}')
print(f'applied to v1 = {rotation@v1}')
print(f'applied to v2 = {rotation@v2}')
