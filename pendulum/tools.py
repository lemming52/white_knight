# Python Packages
import json


def load_config(label=False):
    # Import json configuration file.
    filename = "config/config.json"
    if label is not False:
        filename = "config/config_%s.json" % label
    with open(filename, 'r') as f:
        config = json.load(f)
    return config
