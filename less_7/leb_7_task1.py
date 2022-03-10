import matplotlib.pyplot as plt
import numpy as np

alpha = np.arange (-2* np.pi, 2* np.pi,0.1)
R=3

x=R* np.cos^3 (alpha)
y=R* np.sin^3 (alpha)

plt.plot (x,y,ls='--',lw=3)

plt.axis('equal')

plt.show()