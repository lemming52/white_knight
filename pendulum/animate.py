# External Packages
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

fig = plt.figure()
plt.axis('square')
ax = plt.axes(xlim=(-2.5, 2.5), ylim=(-2.5, 2.5))
mass1, = ax.plot([], [], 'o', lw=9)
mass2, = ax.plot([], [], 'o', lw=9)
rod1, = ax.plot([], [], lw=2)
rod2, = ax.plot([], [], lw=2)

positions = np.loadtxt('double_positions.txt')
t = positions[:, 0]
x1 = positions[:, 1]
y1 = positions[:, 2]
x2 = positions[:, 3]
y2 = positions[:, 4]


def init():
    return mass1, mass2, rod1, rod2


def animate(i):
    xa, ya, xb, yb = x1[i], y1[i], x2[i], y2[i]
    mass1.set_data([xa], [ya])
    mass2.set_data([xb], [yb])
    rod1.set_data([0.0, xa],  [0.0, ya])
    rod2.set_data([xa, xb],  [ya, yb])
    return mass1, mass2, rod1, rod2

animation = anim.FuncAnimation(fig, animate, init_func=init,
                               frames=len(t), interval=10, blit=True)
plt.show()
