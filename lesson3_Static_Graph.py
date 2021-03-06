import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
y = [0,2,4,6,8,10,12]
z = [0,-2,-4,-6,-8,-10,-12]

#line graph
plt.plot(x, y, 'r-o', label="y = 2x")   #'r-o' -> line of color red with circular marker; OR 'r-^' -> line of color red with triangular marker
                                        #'r--' -> dotted line of color red
plt.plot(x, z, 'b-o', label="z = -2x")

# vertical bar graph
# plt.bar(x, y, label="y = 2x")
# plt.bar(x, z, label="z = -2x")

# horizontal bar graph
# plt.barh(x, y, label="y = 2x")
# plt.barh(x, z, label="z = -2x")

plt.title("Static Graph Example")
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")

plt.grid(True)
plt.legend()    #before enabling legend; assign the label
plt.show()

