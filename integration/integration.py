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
    return variables


def run_monte_carlo(samples, function, func_coeff, func_vars):
    # Master monte-carlo function, runs the main sample loop.
    value = 0
    for i in range(samples):
        value += function(func_vars)
    return value*func_coeff


def sin_monte_element(rmax):
    # Calculate the integrand for a single loop
    value = gen_random_variables(8, 0, rmax)
    result = sin_theta_sum(value)
    return result


def run_single(samples):
    # Function configured to run the particular integral required
    rmax = np.pi/8  # Solely works on same limit intengrals
    volume = np.power(rmax, 8)
    func_coeff = 1000000
    func_vars = rmax
    values = run_monte_carlo(samples,
                             sin_monte_element,
                             func_coeff, func_vars)
    total = volume*values/samples
    return total
