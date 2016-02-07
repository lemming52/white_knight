# Custom Packages
import integration

# External Packages
import numpy as np


def main():
    iterations = 25
    samples = 10000000
    values = [integration.run_single(samples) for i in range(iterations)]
    print(np.average(values))
    print(np.std(values))

main()
