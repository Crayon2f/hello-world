import ConfigParser
import sys

__config = ConfigParser.RawConfigParser()
__config.read(sys.path[1] + '\\config\\prop.ini')


def init():
    return __config
