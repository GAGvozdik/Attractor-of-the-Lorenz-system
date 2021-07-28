import matplotlib.pyplot as plt
import numpy as np

x_0 = 1
y_0 = 3
z_0 = 5

t = 5000
b = 8 / 3
r = 10
sigma = 10
dlina = 100000
step = t / dlina

x = [x_0]
y = [y_0]
z = [z_0]
Xs = []
Ys = []
alpha = 0

for i in range(dlina - 1):
    x.append(0)
    y.append(0)
    z.append(0)
    x[i + 1] = x[i] + step * (sigma * (y[i] - x[i]))
    y[i + 1] = y[i] + step * (x[i] * (r - z[i]) - y[i])
    z[i + 1] = z[i] + step * (x[i] * y[i] - b * z[i])

    Xs.append(y[i + 1] - x[i + 1] * np.sin(alpha) / 2)
    Ys.append(z[i + 1] - x[i + 1] * np.cos(alpha) / 2)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_aspect(1)
ax1.scatter(Xs, Ys, s=0.02, color='blue')

plt.show()
