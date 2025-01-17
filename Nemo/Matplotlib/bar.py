import matplotlib.pyplot as plt
import numpy as np

x = np.array(["white", "Blaack", "Red"])
y = np.array([5, 8,10])

plt.title("Balls")
plt.xlabel("Colour")
plt.ylabel("Quantity")
plt.bar(x,y)
plt.show()