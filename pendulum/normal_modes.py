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


def frequencies(solutions, label, config):
    t = solutions[:, 0]
    theta1 = solutions[:, 1]
    theta2 = solutions[:, 2]
    # Generate the power specctrum of the displacements
    freq_1 = np.power(abs(np.fft.fft(theta1)), 2)
    freq_2 = np.power(abs(np.fft.fft(theta2)), 2)
    timestep = t[1] - t[0]

    freq = 2*np.pi*np.fft.fftfreq(freq_1.size, d=timestep)  # Convert to rads
    coeff = config['g']/config['L1']
    # Calculated predicted frequencies
    mode_freq1 = ((2 + config['initial'][1]/config['initial'][0])*coeff)**(1/2)
    mode_freq2 = ((2 - config['initial'][1]/config['initial'][0])*coeff)**(1/2)

    f, axarr = plt.subplots(2)
    axarr[0].plot(freq, freq_1, label='Theta 1')
    axarr[0].set_ylabel('w^2')
    axarr[0].set_xlim([0, 8])
    axarr[1].plot(freq, freq_2, label='Theta 2')
    axarr[1].set_ylabel('w^2')
    axarr[1].set_xlim([0, 8])
    axarr[1].set_xlabel('w / rad')
    axarr[0].set_title('Power Spectrum for Angular Displacements - %s' % label)
    # Add vertical lines at predicted peak values.
    axarr[0].axvline(mode_freq1, 0, np.amax(freq_1), color='r', label='Prediction 1')
    axarr[1].axvline(mode_freq1, 0, np.amax(freq_2), color='r', label='Prediction 1')
    axarr[0].axvline(mode_freq2, 0, np.amax(freq_1), color='g', label='Prediction 2')
    axarr[1].axvline(mode_freq2, 0, np.amax(freq_2), color='g', label='Prediction 2')
    axarr[0].legend(loc='upper center')
    axarr[1].legend(loc='upper center')
    f.savefig("angular_displacements_freq_%s.png" % label)


def main():
    label = input('Enter config file label (e.g. core): ')
    config = tools.load_config(label)
    solutions = np.loadtxt('double_solutions_%s.txt' % label)
    displacements(solutions, label, config)
    frequencies(solutions, label, config)

main()
