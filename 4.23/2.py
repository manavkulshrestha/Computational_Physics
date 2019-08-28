from numpy.random import randint,randn
import numpy as np
import matplotlib.pyplot as plt

W = 10000

#S = 1
#lim = 5
#plt.title(f'S = {S}: -1 or 1')
#plt.hist([sum(2*randint(2)-1 for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()
#
#plt.title(f'S = {S}: Normal')
#plt.hist([sum(randn() for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()
#
#plt.title(f'S = {S}: [-3,3]')
#plt.hist([sum(6.0*(rand()-.5) for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()
#
#S = 2
#lim = 7
#plt.title(f'S = {S}: -1 or 1')
#plt.hist([sum(2*randint(2)-1 for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()
#
#plt.title(f'S = {S}: Normal')
#plt.hist([sum(randn() for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()
#
#plt.title(f'S = {S}: [-3,3]')
#plt.hist([sum(6.0*(rand()-.5) for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()
#    
#S = 100
#lim = 100
#plt.title(f'S = {S}: -1 or 1')
#plt.hist([sum(2*randint(2)-1 for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()
#
#plt.title(f'S = {S}: Normal')
#plt.hist([sum(randn() for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()
#
#plt.title(f'S = {S}: [-3,3]')
#plt.hist([sum(6.0*(rand()-.5) for s in range(S)) for w in range(W)],bins=linspace(-lim,lim,100))
#plt.show()

for S in [1,2,100]:
    plt.title(f'S = {S}: -1 or 1')
    plt.hist([sum(2*randint(2)-1 for s in range(S)) for w in range(W)])
    plt.show()
    
    plt.title(f'S = {S}: Normal')
    plt.hist([sum(randn() for s in range(S)) for w in range(W)])
    plt.show()
    
    plt.title(f'S = {S}: [-3,3]')
    plt.hist([sum(6.0*(rand()-.5) for s in range(S)) for w in range(W)])
    plt.show()