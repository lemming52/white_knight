# Python Packages
import random

# External Packages
import numpy as np


def sin_theta_sum(variables):
    theta = 0
    for var in variables:
        theta += var
    return np.sin(theta)


def gen_random_variables(count, rmin, rmax):
    variables = []
    for i in range(count):
        variables.append(np.random.uniform(rmin, rmax))
        # test_range(rmin, rmax, value)
    return variables


def run_monte_carlo(samples, function, func_coeff, func_vars):
    value = 0
    for i in range(samples):
        if i % 10000 == 0:
            print(i)
        value += function(func_vars)
    value = value*func_coeff/samples
    return value


def sin_monte_element(rmax):
    value = gen_random_variables(8, 0, rmax)
    result = sin_theta_sum(value)
    return result


def main():
    rmax = np.pi/8
    samples = 10000000
    coefficient = 1000000
    volume = np.power(rmax, 8)
    func_coeff = coefficient*volume
    func_vars = rmax
    result = run_monte_carlo(samples, sin_monte_element, func_coeff, func_vars)
    print(result)


def test_range(rmin, rmax, value):
    if (value <= rmin or value >= rmax):
        print(False)


main()
