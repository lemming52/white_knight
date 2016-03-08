# External Packages
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

# Custom Packages
import tools

# Get input to designate system for plotting
label = input('Enter config file label (e.g. core): ')
config = tools.load_config(label)
fig = plt.figure()
plt.axis('square')

# Define limits of plot relative to the lengths of the rods
lim = (config['L1'] + config['L2'])*1.25

ax = plt.axes(xlim=(-lim, lim), ylim=(-lim, lim))
mass1, = ax.plot([], [], 'o', lw=9)
mass2, = ax.plot([], [], 'o', lw=9)
rod1, = ax.plot([], [], lw=2)
rod2, = ax.plot([], [], lw=2)

positions = np.loadtxt('data/double_positions_%s.txt' % label)
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
                               frames=len(t),
                               interval=config['interval'],
                               blit=True)
plt.show()
