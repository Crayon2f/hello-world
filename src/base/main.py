# coding=utf-8
from itertools import imap
import os

from decimal import Decimal

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
uv_set = {'1', ',', '0000', '444', '1'}
uv_set.add('333')
print 'set = ', uv_set

a = '''111
222'''
b = r'''111
222'''
print a
print b

print '小铜人机器人'

# file_path = r'C:\Users\feifan.gou\Desktop\readme.txt'
#
# f = open(file_path, 'r')
# print os.path.exists(file_path)

a = "abcdefghij klmn"

print 'hello %-7s' % 'come'

print a.isalnum()
b = '()&&&%^%'
print b.isalpha()
print a.islower()
print a.isdigit()

print ','.join(imap(str, [0, 9, 8, 7]))

var = {
    '1': 1,
    '2': 2,
    '3': 4
}

print tuple(var.values())

a = 4.5566
print round(a, 2)  # 4.56

print '%.2f' % a

print Decimal('5.125').quantize(Decimal('0.00'))

print 'd' in 'abc'
print 'ab c'.rsplit(' ')

print '@@43@44'.split('@')

print 'DLJD'.lower()

empty_list = []
empty_tuple = ()
empty_dict = {}
empty_str = ''
none = None
zero = 0

if empty_dict or empty_list or empty_str or empty_str or none or zero:
    print '==========='
else:
    print 'these is False'

if not empty_list:
    print 'use not '

temp_dict = {
    'a': 'd',
    'b': 'd',
    'v': 'd',
    'd': 'd'
}
for key in temp_dict:
    print key, '====', temp_dict[key]

list_ = {'d', 'd', 's'}
print list_

list_num = [1, 2, 3, 4]

list__ = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num if (j != i and k != j and k != i)]

print (list__)

print [(x, y, z) for x in range(1, 5) for y in range(1, 5) for z in range(1, 5) if (x != y) and (x != z) and (y != z)]

print os.path.join('d:\\downloads\\video', 'polaris.mp4')
