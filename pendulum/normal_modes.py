# External Packages
import numpy as np
import matplotlib.pyplot as plt

# Custom Packages
import tools


def displacements(solutions, label, config):
    t = solutions[:, 0]
    theta1 = solutions[:, 1]
    theta2 = solutions[:, 2]
    sim_time = config['sim_time']

    plt.figure()
    plt.plot(t, theta1, label='Theta 1')
    plt.plot(t, theta2, label='Theta 2')
    plt.xlim([0, sim_time/6])  # Arbitrary scaling
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('Angular Displacement / rads')
    plt.title('Angular Displacement against time for both Masses : %s' % label)
    plt.savefig('angular_displacements_%s.png' % label)


def main():
    label = input('Enter config file label (e.g. core): ')
    config = tools.load_config(label)
    solutions = np.loadtxt('double_solutions_%s.txt' % label)
    displacements(solutions, label, config)
    positions = np.loadtxt('double_positions_%s.txt' % label)

main()
