# External Packages
import matplotlib.pyplot as plt
import numpy as np

# Custom Packages
import tools


def gen_aperture_1d(length):
    # Create an aray of complex zeros
    return np.array(np.zeros(length), dtype=complex)


def aperture_1d(aperture, half_width, centre, conversion, ap_func, args):
    # Convert the zero aperture into an actual aperture using ap_func.
    ap_min = centre - half_width
    ap_max = centre + half_width
    i = np.array(range(ap_max-ap_min))  # sub-array with width of slit

    aperture[ap_min: ap_max] = ap_func(i, half_width, conversion, args)
    return aperture


# APERTURE FUNCTIONS
def get_func(name):
    # Convert the config specification to apropriate function
    # Probably a better way
    if name == 'slit':
        return slit
    elif name == 'grating':
        return grating
    else:
        print("I don't know that function")
        return None


def slit(i, half_width, *args):
    # Plain empty slit, full transmission
    return complex(1, 0)


def grating(i, half_width, conversion, args):
    # Sinusoidal phase grating
    s = args['s']
    m = args['m']
    # Convert the slit sub array into x measurements.
    x = (i-half_width)*conversion
    # Return complex number
    phase = np.exp(1j*m*np.sin(2*np.pi*x/s)/2)
    return phase


def evaluate(config, ap_func, correction, label):
    """
    Master function
    config - dictionary containing the apeture configuration info
    ap_func - function for calculating the complex aperture at a point
    correction - bool: designates if correcting for fresnel
    label - system/ exercise identifier
    """

    N = 2097152  # Samples for the aperture / Resolution, power of 2

    aperture = gen_aperture_1d(N)

    conversion = config['extent'] / N  # Calculate distance per sample

    # Convert measurements to bin counts
    half_width = convert(config['width']/2, conversion)
    centre = convert(config['centre'], conversion)

    distance = config['distance']
    wavelength = config['wavelength']
    args = config['args']
    aperture = aperture_1d(aperture, half_width, centre,
                           conversion, ap_func, args)

    if correction:
        # Apply fresnel correction if needed.
        aperture = correct(aperture, wavelength, distance, conversion)

    amplitude = conversion*np.fft.fft(aperture)
    # Shift fft so graph plots properly
    amplitude = np.fft.fftshift(amplitude)

    # No 2pi as fft.freq gives regular as opposed to angular freq.
    y = distance*wavelength*np.fft.fftfreq(amplitude.size,
                                           d=conversion)
    y = np.fft.fftshift(y)

    plot(amplitude, y, config, label)


def convert(value, conversion):
    # Convert measurement into whole number of bins
    # There is a degree of inaccuracy here
    return round(value / conversion)


def correct(aperture, wavelength, distance, conversion):
    # Apply the fresnel correction to the aperture.
    i = np.array(range(aperture.size))
    x = (i-len(aperture)/2)*conversion  # Get x for entire aperture
    correction = np.exp(1j*np.pi*np.power(x, 2)/(distance*wavelength))
    return correction*aperture


def plot(amplitude, y, config, label):
    # Plot the diffraction pattern

    intensity = np.power(abs(amplitude), 2)  # Convert to intensity
    intensity = intensity/np.amax(intensity)

    plt.figure()

    if config['predicted'] is not False:
        # Plot the predicted sinc function if single slits
        plt.plot(y, predicted(y, config), label='Predicted')
    plt.plot(y, intensity, color='r', label='Calculated')

    plt.xlim(-config['lim'], config['lim'])
    plt.ylim(0, 1.1)
    plt.xlabel('y / m')
    plt.ylabel('Fractional Intensity compared to Maximum')
    plt.title('Diffaction Pattern: %s, D=%sm' % (config['ap_func'],
                                                 config['distance']))
    plt.legend()
    plt.savefig('pattern_%s.png' % label)


def predicted(y, config):
    # Single slit sinc intensity function
    factor = config['width']*y/(config['wavelength']*config['distance'])
    predicted = np.power(np.sinc(factor), 2)
    return predicted


def main():
    label = input('Enter config file label: ')
    config = tools.load_config(label)
    correction = config['correction']
    ap_func = get_func(config['ap_func'])
    evaluate(config, ap_func, correction, label)


main()
