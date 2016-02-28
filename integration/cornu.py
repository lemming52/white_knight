# Custom Packages
import fresnel

# External Packages
import numpy as np
from scipy.integrate import quad


def coord_pair(u):
    # Calculate the C and S values for a particular u, which give
    # coordinates for the spiral.
    coeff = np.pi/2
    C = quad(fresnel.cos_integrand, 0, u, args=(coeff, ))
    S = quad(fresnel.sin_integrand, 0, u, args=(coeff, ))
    return C[0], S[0]


def cornu():
    u_range = np.linspace(-10, 10, 1000)
    with open('cornu.dat', 'w') as f:
        f.write('u\tC\tS\n')
        for u in u_range:
            C, S = coord_pair(u)
            f.write('%s\t%s\t%s\n' % (u, C, S))
    f.close()


cornu()
