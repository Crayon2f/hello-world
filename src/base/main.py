# coding=utf-8
from itertools import imap
import os

var = {'3': 4, '45': 0}
print var.keys()
print var.values()

a, b, c, d, e, f = 1, 2, 3, 1, 2, 3

var = {(a, b, c): 'sss'}
print var[(d, e, f)]

var = u'4,5,6,76,7,呵呵呵'
print var[::-1]

print ('2', '3') in ('4', '6', '2', '3', '2')

var = [1, 3, 4, 5, 6, 6, [1, 2, 34]]
print [1, 2, 34] in var

# uv_set = set()
uv_set = {'1', ',', '0000', '444'}
uv_set.add('333')
print uv_set

a = '''111
222'''
b = r'''111
222'''
print a
print b

print '小铜人机器人'

file_path = r'C:\Users\feifan.gou\Desktop\readme.txt'

f = open(file_path, 'r')
print os.path.exists(file_path)

a = "abcdefghij klmn"

print 'hello %-7s' % 'come'

print a.isalnum()
b = '()&&&%^%'
print b.isalpha()
print a.islower()
print a.isdigit()

print ','.join(imap(str, [0, 9, 8, 7]))
