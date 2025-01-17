#Visulalisation of data
#Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,3,6,8])
ypoints = np.array([0,55,250,2])

plt.plot(xpoints, ypoints)
plt.show()