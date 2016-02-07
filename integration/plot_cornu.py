# External Packages
import matplotlib.pyplot as plt

# Custom Packages
import plot


def cornu_plot(C, S):
    plt.figure()
    plt.plot(S, C)
    plt.xlabel('S')
    plt.ylabel('C')
    plt.title('Cornu Spiral')
    plt.savefig("cornu.png")


def main():
    U, C, S = plot.load('cornu.dat')
    cornu_plot(C, S)

main()
