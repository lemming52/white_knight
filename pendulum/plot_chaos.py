# External Packages
import matplotlib.pyplot as plt
import numpy as np


def plot(label, i, cmap):
    # Plot the mass positions for all times, giving trajectories
    positions = np.loadtxt('data/double_positions_%s%s.txt' % (label, i,))
    m1 = positions[:1000, 1:3]
    m2 = positions[:1000, 3:5]

    plt.plot(m1[:, 0], m1[:, 1], color=cmap(i/100), lw=0.3)
    plt.plot(m2[:, 0], m2[:, 1], color=cmap(i/100), lw=0.3)


def disp(label, i, cmap):
    solutions = np.loadtxt('data/double_solutions_%s%s.txt' % (label, i, ))
    t = solutions[:1000, 0]
    theta1 = solutions[:1000, 1]
    theta2 = solutions[:1000, 2]
    plt.plot(t, theta2, color=cmap(i/100), lw=0.3)
    plt.plot(t, theta1, color=cmap(i/100), lw=0.3)


def main():
    label = input('Enter config file label (e.g. rand, pert): ')
    plt.figure()
    cmap = plt.get_cmap('jet')
    for i in range(0, 100):
        plot(label, i, cmap)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Chaotic Double Pendulum Trajectories: %s' % label)
    plt.savefig('positions_chaotic_%s.png' % label)
    plt.figure()
    for i in range(0, 100):
        disp(label, i, cmap)
    plt.xlabel('t')
    plt.ylabel('theta')
    plt.title('Chaotic Angular Displacements: %s' % label)
    plt.savefig('displacements_chaotic%s.png' % label)

main()
