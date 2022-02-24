import matplotlib.pyplot as pit
import numpy as np

def circle_plotter (radius=10):
  x=np.arande(-2*radius, 4*radius, 0.2)
  x=np.arande(-2*radius, 8*radius, 0.2)

  X,Y=np.meshgrid (x,y)
  fxy = X**2+ Y**2
  plt.contour (X,Y,txy ,levels=[radius**2.5])

parabola_plotter()