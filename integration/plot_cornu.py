# External Packages
import matplotlib.pyplot as plt

# Custom Packages
from tools import load


def cornu_plot(C, S):
    plt.figure()
    plt.plot(C, S)
    plt.xlabel('C')
    plt.ylabel('S')
    plt.title('Cornu Spiral')
    plt.savefig("cornu.png")


def main():
    U, C, S = plot.load('cornu.dat')
    cornu_plot(C, S)

main()
