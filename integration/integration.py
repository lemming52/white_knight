# Python Packages
import random

# External Packages
import numpy as np


def sin_theta_sum(variables):

    theta = 0
    for var in variables:
        theta += var
    return np.sin(theta)


def gen_random_list(count, rmin, rmax):
    variables = []
    for i in range(count):
        value = np.random.uniform(rmin, rmax)
        variables.append(value)
        test_range(rmin, rmax, value)
    return variables


def run_monte_carlo(samples):
    return False


def main():
    rmax = np.pi/8
    variables = gen_random_list(7, 0, rmax)
    result = sin_theta_sum(variables)
    print(variables)
    print(result)


def test_range(rmin, rmax, value):
    if (value <= rmin or value >= rmax):
        print(False)


main()
