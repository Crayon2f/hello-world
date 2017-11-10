import ConfigParser
import sys

config = ConfigParser.RawConfigParser()
config.read(sys.path[1] + '\\config\\prop.ini')


def init():
    return config
