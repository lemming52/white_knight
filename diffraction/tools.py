# Python Packages
import json


def load_config(label=None):
    # Import json configuration file.
    filename = "config/config.json"  # Base config file
    if label is not None:
        filename = "config/config_%s.json" % label
    with open(filename, 'r') as f:
        config = json.load(f)
    return config
