import numpy as np
import matplotlib.pylab as pl
x = np.linspace(0,1)
y = np.sin(4*np.pi*x)*np.exp(-5*x)
pl.plot(x,y,'o')
pl.show()