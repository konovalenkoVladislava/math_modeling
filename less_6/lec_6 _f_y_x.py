import matplotlib.pyplot as pit
import numpy as np

def circle_plotter (radius=10)
  x=np.arande(-2*radius, 2*radius, 0.1)
  x=np.arande(-2*radius, 2*radius, 0.1)

  X,Y=np.meshgrid (x,y)
  fxy = X**2+ Y**2
  plt.contour (X,Y,txy ,levels=[0])
  plt.axis ()
parabola_plotter()