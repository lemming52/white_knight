# External Packages
import numpy as np


def gen_random_array(num_count, rmin, rmax, length, iterations):
    # Make use of numpy to generate an array of random numbers
    array = np.random.uniform(rmin, rmax, (iterations, length, num_count))
    return array


def sin_theta_sum(rand_array, coeff):
    values = np.sin(np.sum(rand_array, axis=2))
    averages = coeff*np.average(values, axis=1)
    return np.average(averages), np.std(averages)


def evaluate(samples, iterations):
    rmin = 0
    rmax = np.pi/8
    volume = np.power(rmax, 8)
    coeff = 1000000*volume
    rand_array = gen_random_array(8, rmin, rmax, samples, iterations)
    value, error = sin_theta_sum(rand_array, coeff*volume)
    return value, error


def main():
    value, error = evaluate(10000000, 2)
    print(value)
    print(error)


main()
