import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
z = []

#1. Populate x and y values
for i in np.arange(0, 2*np.pi, (2*np.pi)/1000):
    x.append(i)
    y.append(np.sin(i))
    z.append(np.sin(i + (np.pi)/2))

#2. Plot graph
plt.plot(x, y, 'r', label = "y = sinx")
plt.plot(x, z, 'g', label = "y = sin(x + pi/2")

plt.axis([0,6.5,-1.2,1.2])  #specify where graph starts and ends; horizontal and vertical limits -> plt.axis([x_min, x_max, y_min, y_max)

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Sin Graph")
plt.legend()
plt.grid(True)

plt.show()
