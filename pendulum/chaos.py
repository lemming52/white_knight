# Custom packages
import pendulum


def main():
    label_base = input('Enter config file label (e.g. rand, pert): ')
    for i in range(0, 100):
        label = ''.join([label_base, str(i)])
        pendulum.evaluate(label)
main()
