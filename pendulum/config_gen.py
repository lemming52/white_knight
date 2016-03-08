# Python Packages
import json

# External Packages
import numpy as np

# Custom Packages
import tools


def gen_initial():
    theta1, theta2 = np.random.uniform(-3*np.pi/2, 3*np.pi/2, 2)
    v1, v2 = np.random.uniform(-0.2, 0.2, 2)
    return [theta1, theta2, v1, v2]


def rand():
    config_main = tools.load_config()
    for i in range(0, 100):
        config = config_main
        config['initial'] = gen_initial()
        with open('config_rand%s.json' % i, 'w') as f:
            json.dump(config, f)
        f.close()


def pert():
    config_main = tools.load_config()
    for i in range(0, 100):
        config = config_main
        config['initial'][1] = config['initial'][1]+0.035
        with open('config_pert%s.json' % i, 'w') as f:
            json.dump(config, f)
        f.close()
        config_main = config


def main():
    #rand()
    pert()


main()
