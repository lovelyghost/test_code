import numpy as np
import matplotlib.pyplot as plt
# func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
# func1 = func.deriv(m=1)
#
# x = np.linspace(-10, 10, 30)
# y = func(x)
# y1 = func1(x)
# plt.plot(x, y,'ro', x, y1, 'g--')
# plt.xlabel('x')
# plt.ylabel('y(x)')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
# x = np.linspace(-10, 10, 30)
# y = func(x)
# func1 = func.deriv(m=1)
# y1 = func1(x)
# func2 = func.deriv(m=2)
# y2 = func2(x)
# plt.subplot(311)
# plt.plot(x, y, 'r-')
# plt.title("Polynomial")
# plt.subplot(312)
# plt.plot(x, y1, 'b^')
# plt.title("First Derivative")
# plt.subplot(313)
# plt.plot(x, y2, 'go')
# plt.title("Second Derivative")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2
ax.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.YlGnBu_r)
plt.show()