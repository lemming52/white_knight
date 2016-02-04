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
            print(i)  # Status Output
        value += function(func_vars)
    return value*func_coeff


def sin_monte_element(rmax):
    value = gen_random_variables(8, 0, rmax)
    result = sin_theta_sum(value)
    return result


def run_single(samples):
    rmax = np.pi/8
    volume = np.power(rmax, 8)
    func_coeff = 1000000
    func_vars = rmax
    values = run_monte_carlo(samples,
                             sin_monte_element,
                             func_coeff, func_vars)
    total = volume*values/samples
    return total
