
import matplotlib.pyplot as plt
import numpy as np

def Gap_plotter(a=1,title = 'Gep plotter'):

  x=np.arange(0.01,10,0.01)
  y=a/x
  plt.plot(x,y, label='gep')
  plt.show()
   

Gep_plotter()    