import numpy as np
import matplotlib.pyplot as plt
# The two useful functions in numpy:
#   1. arange() -> np.arange(initial, final, increment)
#                  arange() function excludes the final number
#   2. linspace() -> np.linspace(initial, final, num_of_points )
#                   num_of_points are the number of points/steps to make to reach final number
#                   linspace() function includes the final number

# x = np.arange(-4, 4, 0.25)
# print(x)
# z = np.linspace(-4, 4, 25)
# print(z)

# Drawing a graph:
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)

m = np.sin(x + np.pi/2)
n = np.cos(x + np.pi/2)

#subplot() -> used to draw plots on separate axes
plt.subplot(2,2,1) # the figure has 2rows and 2columns; 1st plot
plt.plot(x, y, 'r', label="y = sin(x)")
plt.legend()

plt.subplot(2,2,2) # the figure has 2rows and 2columns; 2nd plot
plt.plot(x, z, 'g', label="y = cos(x)")
plt.legend()

plt.subplot(2,2,3) # the figure has 2row and 2columns; 3rd plot
plt.plot(x, m, 'b', label="y = sin(x) + 90")
plt.legend()

plt.subplot(2,2,4) # the figure has 2row and 2columns; 4th plot
plt.plot(x, n, 'y', label="y = cos(x) + 90")
plt.legend()

plt.show()
