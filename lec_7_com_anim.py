import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax = plt.subplots()
boll,=plt.plot([], [], 'o', color='r', label='Boll')

def circle _move (R ,vx0, vy, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange (0, 2*np.pi, 0.1)
    x= x0 + R*np.cos(alpha)
    y= y0 + R*np.cos(alpha)
    return x,y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)

def animate(i) :
    ball.set_data(circle_move(R=5, vx0=0.01, xy0=0.01, time=i))

ani = animation.FuncAnimation(
  
)