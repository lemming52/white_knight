# External Packages
import numpy as np


def cos_integrand(x, coeff):
    return np.cos(np.power(x, 2)*coeff)


def sin_integrand(x, coeff):
    return np.sin(np.power(x, 2)*coeff)
