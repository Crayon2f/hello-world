# coding:utf-8
import configparser
import os

__config = configparser.RawConfigParser()
__config.read(os.path.join(os.getcwd(), '..', '..', 'config', 'prop.ini'))
CONFIG = __config
