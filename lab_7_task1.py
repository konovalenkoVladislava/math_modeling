import matplotlib.pyplot as plt
import numpy as np

t = np.arange (-2* np.pi, 2* np.pi,0.1)
R=100


x = R * (t-(np.sin(t)))
y = R * (1-(np.cos(t)))

plt.plot (x,y,ls = '-',)
plt.axis('equal')
plt.show()