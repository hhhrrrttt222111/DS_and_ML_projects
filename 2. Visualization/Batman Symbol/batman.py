import matplotlib.pyplot as plt
import numpy as np
import math


Y = np.arange(-4, 4, .005)
X = np.zeros(0)

for y in Y:
    X = np.append(X, abs(y / 2) - 0.09137 * y ** 2 + math.sqrt(1 - (abs(abs(y) - 2) - 1) ** 2) - 3)

Y1 = np.append(np.arange(-7, -3, .01), np.arange(3, 7, .01))
X1 = np.zeros(0)

for y in Y1:
    X1 = np.append(X1, 3 * math.sqrt(-(y / 7) ** 2 + 1))

X = np.append(X, X1)
Y = np.append(Y, Y1)
Y1 = np.append(np.arange(-7., -4, .01), np.arange(4, 7.01, .01))
X1 = np.zeros(0)

for y in Y1:
    X1 = np.append(X1, -3 * math.sqrt(-(y / 7) ** 2 + 1))

X = np.append(X, X1)
Y = np.append(Y, Y1)
Y1 = np.append(np.arange(-1, -.8, .01), np.arange(.8, 1, .01))
X1 = np.zeros(0)

for y in Y1:
    X1 = np.append(X1, 9 - 8 * abs(y))

X = np.append(X, X1)
Y = np.append(Y, Y1)
Y1 = np.arange(-.5, .5, .05)
X1 = np.zeros(0)

for y in Y1:
    X1 = np.append(X1, 2)

X = np.append(X, X1)
Y = np.append(Y, Y1)
Y1 = np.append(np.arange(-2.9, -1, .01), np.arange(1, 2.9, .01))
X1 = np.zeros(0)

for y in Y1:
    X1 = np.append(X1, 1.5 - .5 * abs(y) - 1.89736 * (math.sqrt(3 - y ** 2 + 2 * abs(y)) - 2))

X = np.append(X, X1)
Y = np.append(Y, Y1)
Y1 = np.append(np.arange(-.7, -.45, .01), np.arange(.45, .7, .01))
X1 = np.zeros(0)

for y in Y1:
    X1 = np.append(X1, 3 * abs(y) + .75)

X = np.append(X, X1)
Y = np.append(Y, Y1)


plt.plot(Y, X, 'yo')
ax = plt.gca()
ax.set_facecolor((0, 0, 0))

plt.plot(Y, X, 'go')  # change color
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.show()

