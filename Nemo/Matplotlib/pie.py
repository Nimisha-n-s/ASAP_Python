import matplotlib.pyplot as plt
import numpy as np


x = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.subplot(1, 2, 1) 
plt.plot(x)
plt.title("Fruits")
 
y= np.array([5, 8, 10]) 
mylabels2 = ["white", "Black", "Red"]  
mycolors = ["#C0C0C0", "k", "r",]
plt.pie(y, labels=mylabels2,colors = mycolors)

plt.subplot(1, 2, 2) 
plt.plot(y)
plt.title("Balls")



plt.suptitle("MY SHOP")
plt.show()
