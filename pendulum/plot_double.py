#External Packages
import matplotlib.pyplot as plt
import numpy as np


def plot_pendulum(label):
    # Plot the mass positions for all times, giving trajectories
    positions = np.loadtxt('data/double_positions_%s.txt' % label)
    m1 = positions[:, 1:3]
    m2 = positions[:, 3:5]
    plt.figure()
    plt.plot(m1[:, 0], m1[:, 1], label='Mass 1')
    plt.plot(m2[:, 0], m2[:, 1], label='Mass 2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Double Pendulum Trajectories: %s' % label)
    plt.legend()
    plt.savefig('positions_%s.png' % label)


def plot_energy(label):
    # Plot the energy variation
    energies = np.loadtxt('data/double_energies_%s.txt' % label)
    t = energies[:, 0]
    E_total = np.sum(energies[:, 1:5], axis=1)  # Sum all energy components

    # Zoomed in plot
    # Divide the deviation from initial by the initial
    E_var = (E_total-E_total[0])/E_total[0]
    plt.figure()
    plt.plot(t, E_var)
    plt.xlabel('t')
    plt.ylabel('Fractional Energy Deviation against Initial')
    plt.title('Energy Variation against Time: %s' % label)
    plt.savefig('energies_%s.png' % label)

    # Zoomed out plot
    plt.figure()
    plt.plot(t, E_total)
    plt.xlabel('t')
    plt.ylabel('Total Energy')
    # Generate limits from data
    plt.ylim([E_total[0]*1.1, 0])  # Negative defined energy
    plt.title('Energy Variation against Time: %s' % label)
    plt.savefig('energies_%s_wide.png' % label)


def main():
    label = input('Enter config file label (e.g. core): ')
    plot_pendulum(label)
    plot_energy(label)


main()

