# Custom Packages
from plot import load

# External Packages
import matplotlib.pyplot as plt


def combined_plot(x, mags, phase, D):
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(x, mags)
    axarr[0].set_ylabel('Amplitude')
    axarr[1].plot(x, phase)
    axarr[1].set_ylabel('Phase')
    axarr[0].set_xlabel('x')
    f.savefig("diffraction_%scm.png" % D)


def plot_length(D):
    x, mags, phase = load('diffraction_%scm.dat' % D)
    combined_plot(x, mags, phase, D)


def main():
    distances = [30, 50, 100]
    for D in distances:
        plot_length(D)

main()
