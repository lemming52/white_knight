#External Packages
import matplotlib.pyplot as plt
import numpy as np


def plot_pendulum(m1, m2):
    plt.figure()
    plt.plot(m1[:, 0], m1[:, 1])
    plt.plot(m2[:, 0], m2[:, 1])
    plt.savefig('positions.png')


def plot_energy():
    energies = np.loadtxt('double_energies.txt')
    t = energies[:, 0]
    E_total = np.sum(energies[:, 1:5], axis=1)
    plt.figure()
    plt.plot(t, E_total)
    plt.savefig('energies.png')


def main():
    positions = np.loadtxt('double_positions.txt')
    m1 = positions[:, 1:3]
    m2 = positions[:, 3:5]
    plot_pendulum(m1, m2)
    plot_energy()


main()
