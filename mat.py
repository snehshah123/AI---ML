import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10)
y=x+1

plt.title("Matplotlib demo ")
plt.xlabel("Time")
plt.ylabel("Speed")

plt.plot(x,y,linestyle="-",color="r")

plt.show()
