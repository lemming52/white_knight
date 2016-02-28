# External Packages
import numpy as np


def gen_random_array(num_count, rmin, rmax, length, iterations):
    # Make use of numpy to generate an array of random numbers
    array = np.random.uniform(rmin, rmax, (length, num_count))
    return array


def sin_theta_sum(rand_array, coeff):
    # Given array of random numbers sin the sum of rows and multiply bu coeff
    values = np.sin(np.sum(rand_array, axis=1))
    average = coeff*np.average(values)
    return average


def evaluate(samples, iterations):
    # Execute a number of iterations for a certain sample size
    rmin = 0
    rmax = np.pi/8
    volume = np.power(rmax, 8)
    coeff = 1000000*volume
    values = []
    for i in range(iterations):
        rand_array = gen_random_array(8, rmin, rmax, samples, iterations)
        value = sin_theta_sum(rand_array, coeff)
        values.append(value)
    return np.average(values), np.std(values, ddof=1)  # STD of sample not Pop


def main():
    # Generate a single value as required
    value, error = evaluate(10000000, 25)
    print(value)
    print(error)
    # Run method for values up to 10^7
    samples = [int(np.rint(np.power(10, (i+1)/2))) for i in range(14)]
    with open('samples.dat', 'w') as f:
        f.write('Samples\tValue\tError\n')
    f.close()
    for sample in samples:
        value, error = evaluate(sample, 25)
        with open('samples.dat', 'a') as f:
            f.write('%s\t%s\t%s\n' % (sample, value, error))
        f.close()

main()
