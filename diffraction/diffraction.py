# External Packages
import matplotlib.pyplot as plt
import numpy as np

# Custom Packages
import tools


def gen_aperture_1d(length):
    return np.array(np.zeros(length), dtype=complex)


def aperture_1d(aperture, half_width, centre, conversion, ap_func, args):
    ap_min = centre - half_width
    ap_max = centre + half_width
    i = np.array(range(ap_max-ap_min))

    aperture[ap_min: ap_max] = ap_func(i, half_width, conversion, args)
    return aperture


def slit(i, half_width, *args):
    return complex(1, 0)


def grating(i, half_width, conversion, args):
    s = args['s']
    m = args['m']
    x = (i-half_width)*conversion
    phase = np.exp(1j*m*np.sin(2*np.pi*x/s)/2)
    return phase


def evaluate(slit, ap_func, correction, label):

    N = 2097152

    aperture = gen_aperture_1d(N)

    conversion = slit['extent'] / N

    half_width = convert(slit['width']/2, conversion)
    centre = convert(slit['centre'], conversion)

    distance = slit['distance']
    wavelength = slit['wavelength']
    args = slit['args']
    aperture = aperture_1d(aperture, half_width, centre,
                           conversion, ap_func, args)

    if correction:
        aperture = correct(aperture, wavelength, distance, conversion)

    amplitude = conversion*np.fft.fft(aperture)
    amplitude = np.fft.fftshift(amplitude)

    # No 2pi as fft.freq gives regular as opposed to angular freq.
    y = distance*wavelength*np.fft.fftfreq(amplitude.size,
                                           d=conversion)
    y = np.fft.fftshift(y)

    plot(amplitude, y, slit, label)


def convert(value, conversion):
    return round(value / conversion)


def correct(aperture, wavelength, distance, conversion):
    i = np.array(range(aperture.size))
    x = (i-len(aperture)/2)*conversion
    correction = np.exp(1j*np.pi*np.power(x, 2)/(distance*wavelength))
    return correction*aperture


def get_func(name):
    if name == 'slit':
        return slit
    elif name == 'grating':
        return grating
    else:
        print("I don't know that function")


def plot(amplitude, y, slit, label):

    intensity = np.power(abs(amplitude), 2)
    intensity = intensity/np.amax(intensity)

    plt.figure()

    if slit['predicted']:
        plt.plot(y, predicted(y, slit), label='Predicted')
    plt.plot(y, intensity, color='r', label='Calculated')

    plt.xlim(-slit['lim'], slit['lim'])
    plt.ylim(0, 1.1)
    plt.xlabel('y / m')
    plt.ylabel('Fractional Intensity compared to Maximum')
    plt.title('Diffaction Pattern: %s, D=%sm' % (slit['ap_func'],
                                                 slit['distance']))
    plt.legend()
    plt.savefig('pattern_%s.png' % label)


def predicted(y, slit):
    factor = slit['width']*y/(slit['wavelength']*slit['distance'])
    predicted = np.power(np.sinc(factor), 2)
    return predicted

def main():
    label = input('Enter config file label: ')
    config = tools.load_config(label)
    correction = config['correction']
    ap_func = get_func(config['ap_func'])
    evaluate(config, ap_func, correction, label)


main()
