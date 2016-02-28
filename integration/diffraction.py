# Custom Packages
from fresnel import cos_integrand, sin_integrand

# External Packages
import numpy as np
from scipy.integrate import quad


def complex_amp(coeff, x1, x2):
    # Calculate the real and imaginary parts of the amplitude at a point.
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
    # Evaluate the fresnel integrals across and beyond the slit.
    slit_min = -width/2  # Define the slit limits
    slit_max = width/2
    x_range = np.linspace(-6*width/2, 6*width/2, 10000)  # Arbitrary range.
    filename = 'diffraction_%scm.dat' % D
    coeff = np.pi/(wavelength*D)
    with open(filename, 'w') as f:
        f.write('x1\tAmplitude\tPhase\n')
        for x in x_range:
            x1 = slit_min - x  # Correct the range to evaluate integral.
            x2 = slit_max - x
            real, imag = complex_amp(coeff, x1, x2)
            mag = magnitude(real, imag)  # Extract amplitude from complex.
            phi = phase(real, imag)
            f.write('%s\t%s\t%s\n' % (x, mag, phi))
    f.close()


def main():
    distances = [30, 50, 100]  # Hard-coded configuration.
    wavelength = 1
    width = 10
    for D in distances:
        slit(width, wavelength, D)

main()
