import numpy as np
import matplotlib.pyplot as plt

ll = 1.0     # size of square L (m)
nn = 50     # grid pts on each edge
dvmax = 0.01 # stop when V changes less than this (V)
om = .875     # over relaxation parameter
a = ll/(nn-1)           # grid spacing (m)
vv = np.zeros((nn,nn))  #  will hold V(x,y) (V)
p = np.copy(vv)

p_0 = -100000 #V/m^2
low, high = int(nn/3), int(2*nn/3)
print(low, high)
for i in range(low,high):
    for j in range(low,high):
        p[i,j] = p_0

# Set V on boundaries:
for j in range(nn):
    vv[0,j] = 100.0      # left edge x=0
    vv[-1,j] = 0     # right edge x=L
for k in range(nn):
    vv[k,0] = 100.00          # bottom edge y=0
    vv[k,-1] = 0         # top edge y=L

# Relaxation calculation
dvvbig = 2*dvmax
sweeps = 0
while dvvbig > dvmax:
    sweeps += 1
    dvvbig = 0.0
    for j in range(1,nn-1):
        for k in range(1,nn-1):
            avn = 0.25*(vv[j+1,k]+vv[j-1,k]+vv[j,k+1]+vv[j,k-1])
#            print(p[j,k])
            dvv = (1+om)*(avn + a*a*p[j,k]/4 - vv[j,k])
            vv[j,k] += dvv
            if abs(dvv)>dvvbig:
                dvvbig = abs(dvv)

# Plot transpose of vv, so y is vertical in plot:
print(f'iterations = {sweeps}')
plt.figure(figsize=(8,5))
plt.imshow(vv.T,origin='lower',extent=(0,ll,0,ll))
plt.colorbar()
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$y$ (m)')
plt.title(r'$V(x,y)$ (V)')
plt.show()