# coding=utf-8

# 时间
import calendar
import time

ticks = time.time()
print '当前时间戳:', ticks

localtime = time.localtime(time.time())
print localtime

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

# print time.clock()
#
# time.sleep(2.5)
#
# print time.clock()

print time.asctime(time.localtime())

print calendar.isleap(int(time.strftime('%Y', time.localtime())))
