# coding:utf-8
import ConfigParser
import os

__config = ConfigParser.RawConfigParser()
__config.read(os.path.join(os.getcwd(), '..', '..', 'config', 'prop.ini'))
CONFIG = __config
