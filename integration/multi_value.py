# Custom Packages
import integration

# External Packages
import numpy as np


def main():
    steps = 14
    with open('samples.dat', 'w') as f:
        f.write('Samples\tValue\tError\n')
    f.close()
    for i in range(steps):
        samples = int(np.rint(np.power(10, (i+1)/2)))
        print(samples)
        #value, error = step(samples)
        #with open('samples.dat', 'a') as f:
        #    f.write('%s\t%s\t%s\n' % (samples, value, error))
        #f.close()


def step(samples):
    iterations = 25
    values = [integration.run_single(samples) for i in range(iterations)]
    return np.average(values), np.std(values)

main()
