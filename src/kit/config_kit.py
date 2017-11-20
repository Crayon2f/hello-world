# coding:utf-8
import ConfigParser
import os

__config = ConfigParser.RawConfigParser()
__config.read(os.path.realpath(__file__) + '\\..\\..\\..\\config\\prop.ini')


def init():
    return __config
