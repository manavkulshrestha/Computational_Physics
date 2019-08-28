import numpy as np
import matplotlib.pyplot as plt

class Mass:
    def __init__(self,x=0,y=0,vx=0,vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.x_hist = [x]
        self.y_hist = [y]

    def step(self,dt=1, count=1):
        if count == 0:
            return
        if self.y < 0:
            self.vx = 0
            self.vy = 0
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.vy -= 9.8*dt
        self.x_hist.append(self.x)#duplication present. intentional
        self.y_hist.append(self.y)#duplication present. intentional
        self.step(dt,count-1)
#a
a = Mass(vx=1,vy=1)
a.step(dt=.01,count=30)

b = Mass(vx=.7,vy=1.3)
b.step(dt=.01,count=30)

plt.title('Point mass trajectories')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(a.x_hist,a.y_hist)
plt.plot(b.x_hist,b.y_hist)
