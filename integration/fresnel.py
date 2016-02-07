# External Packages
import numpy as np
from scipy.integrate import quad


def cos_integrand(x):
    return np.cos(np.pi*np.power(x, 2)/2)


def sin_integrand(x):
    return np.sin(np.pi*np.power(x, 2)/2)


def coord_pair(u):
    C = quad(cos_integrand, 0, u)
    S = quad(sin_integrand, 0, u)
    return C[0], S[0]


def cornu():
    u_range = np.linspace(-10, 10, 1000)
    with open('cornu.dat', 'w') as f:
        f.write('u\tC\tS\n')
        for u in u_range:
            C, S = coord_pair(u)
            print(C)
            f.write('%s\t%s\t%s\n' % (u, C, S))
    f.close()


cornu()
