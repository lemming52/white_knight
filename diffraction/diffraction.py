# External Packages
import matplotlib.pyplot as plt
import numpy as np

# Custom Packages
import tools


def aperture_1d(length):
    return np.array(np.zeros(length), dtype=complex)


def slit_1d(aperture, half_width, centre, conversion, ap_func, *args):
    slit_min = centre - half_width
    slit_max = centre + half_width
    print(slit_min+slit_max)
    ap = np.array([ap_func(i, half_width, args) for i in range(slit_max - slit_min)])
    aperture[slit_min: slit_max] = ap
    return aperture


def hole(i, width, *args):
    return complex(1, 0)


def grating(i, width, conversion, args):
    s = args['s']
    m = args['m']
    return complex(1, m/2*np.sin(2*np.pi*(i-width)*conversion/s))


def evaluate(slit, ap_func, correction, label):
    aperture = aperture_1d(262144)

    conversion = slit['extent'] / 262144
    half_width = round(slit['width'] /(2*conversion))
    centre = round(slit['centre'] / conversion)
    distance = slit['distance']
    args = slit['args']
    wavelength = slit['wavelength']
    aperture = slit_1d(aperture, half_width, centre, conversion, ap_func, args)
    if correction:
        aperture = correct(aperture, wavelength, distance)
    amplitude = conversion*np.fft.fft(aperture)
    y = distance*wavelength/(2*np.pi)*np.fft.fftfreq(amplitude.size, d=conversion)
    plot(amplitude, y, slit, conversion)


def get_func(name):
    if name == 'hole':
        return hole
    elif name == 'grating':
        return grating
    else:
        print("I don't know that function")


def plot(amplitude, y, slit, conversion):
    factor = slit['width']*np.pi*y/(slit['wavelength']*slit['distance'])
    predicted = conversion*np.power(np.sin(factor)/factor, 2)
    plt.figure()
    intensity = np.power(abs(amplitude), 2)
    plt.plot(y, intensity, color='r')
    plt.plot(y, predicted)
    plt.xlim(-100*slit['width'], 100*slit['width'])
    plt.show()


def main():
    label = input('Enter config file label: ')
    config = tools.load_config(label)
    correction = config['correction']
    ap_func = get_func(config['ap_func'])
    evaluate(config, ap_func, correction, label)


main()
