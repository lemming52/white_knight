# Custom Packages
from fresnel import cos_integrand, sin_integrand

# External Packages
import numpy as np
from scipy.integrate import quad


def complex_amp(coeff, x1, x2):
    real = quad(cos_integrand, x1, x2, args=(coeff, ))
    imaginary = quad(sin_integrand, x1, x2, args=(coeff, ))
    return real[0], imaginary[0]


def magnitude(real, imag):
    real = np.power(real, 2)
    imag = np.power(imag, 2)
    return(np.power(real + imag, 1/2))


def phase(real, imag):
    return np.arctan(real/imag)


def slit(width, wavelength, D):
    x_range = np.linspace(-width/2, width/2, 10000)
    filename = 'diffraction_%scm.dat' % D
    coeff = np.pi/(wavelength*D)
    with open(filename, 'w') as f:
        f.write('x1\tAmplitude\tPhase\n')
        for x in x_range:
            x2 = width/2 - x
            x1 = -width/2 - x
            real, imag = complex_amp(coeff, x1, x2)
            mag = magnitude(real, imag)
            phi = phase(real, imag)
            f.write('%s\t%s\t%s\n' % (x1, mag, phi))
    f.close()


def main():
    distances = [30, 50, 100]
    wavelength = 1
    width = 10
    for D in distances:
        slit(width, wavelength, D)

main()
