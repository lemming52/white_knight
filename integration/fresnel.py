# External Packages
import numpy as np

# Functions for evaluating the fresnel integrals.


def cos_integrand(x, coeff):
    return np.cos(np.power(x, 2)*coeff)


def sin_integrand(x, coeff):
    return np.sin(np.power(x, 2)*coeff)
