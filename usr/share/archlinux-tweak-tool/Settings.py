#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

import configparser
from Functions import config

settings = config


def make_file(section, key):
    config = configparser.ConfigParser()
    config[section] = key
    with open(settings, 'w') as configfile:
        config.write(configfile)


def new_settings(section, key):
    config = configparser.ConfigParser()
    config.read(settings)
    config[section] = key

    with open(settings, 'w') as configfile:
        config.write(configfile)


def write_settings(section, key, value):
    config = configparser.ConfigParser()
    config.read(settings)

    config[section][key] = value
    with open(settings, 'w') as configfile:
        config.write(configfile)


def read_section():
    config = configparser.ConfigParser()
    config.read(settings)

    return config.sections()


def read_settings(section, key):
    config = configparser.ConfigParser()
    config.read(settings)

    return config[section][key]
