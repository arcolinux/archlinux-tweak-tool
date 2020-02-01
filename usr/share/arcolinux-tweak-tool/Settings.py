#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================

import configparser
import os
from Functions import home

settings = home + "/.config/arcolinux-tweak-tool/settings.conf"

def make_file(section, key):
    config = configparser.ConfigParser()
    config[section] = key
    with open(settings, 'w') as configfile:
        config.write(configfile)

def write_settings(section, key):
    config = configparser.ConfigParser()
    config.read(settings)

    config[section] = key
    with open(settings, 'w') as configfile:
        config.write(configfile)

def read_settings(section, key):
    config = configparser.ConfigParser()
    config.read(settings)

    return config[section][key]
