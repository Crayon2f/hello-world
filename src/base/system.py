# coding=utf-8
import os
import sys

for p in sys.path:
    print p

print os.path.realpath(__file__)


