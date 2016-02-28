# External Packages
import matplotlib.pyplot as plt
import numpy as np


def load(filename):
    # Load and store a 3 value file.
    # Multipurpose beyond ('samples, values errors')
    # I know I'm bad.
    samples = []
    values = []
    errors = []
    with open(filename, 'r') as f:
        lines = list(f)
    f.close()
    for line in lines[1:]:
        line = line.split('\t')
        samples.append(float(line[0]))
        values.append(float(line[1]))
        errors.append(float(line[2]))

    return samples, values, errors


def value_plot(samples, values, errors):
    plt.figure()
    plt.plot(samples, values, label='Calculated')
    plt.plot(samples, [537.1873 for i in range(len(samples))],
             label='True Value')
    plt.errorbar(samples, values, yerr=errors)
    plt.xlabel('Number of Monte-Carlo Samples')
    plt.xscale('log')
    plt.ylabel('Integral Estimate')
    plt.title('Estimated Value against Number of Monte-Carlo Samples')
    plt.legend()
    plt.savefig("values.png")


def error_plot(samples, errors):
    constant = errors[0]/(np.power(samples[0], -1/2))
    samples = np.log10(samples)
    errors = np.log10(errors)
    plt.figure()
    plt.plot(samples, errors, label='Calculated error')
    plt.plot(samples, np.log10(constant) + samples*-1/2, label='Predicted error')
    plt.xlabel('Log of Monte-Carlo Samples')
    plt.ylabel('Log of Error in Estimate')
    plt.title('Log-Log plot of Error against Samples showing -1/2 gradient')
    plt.legend()
    plt.savefig('errors.png')


def main():
    samples, values, errors = load('samples.dat')
    value_plot(samples, values, errors)
    error_plot(samples, errors)

main()
