import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 90, 95, 100, 85,105, 110, 115, 120, 125])
y = np.array([240, 260, 270, 280,250, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Distance")
plt.ylabel("Time")

plt.show()