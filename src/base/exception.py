# coding=utf8

try:
    print(4 / 1)
except ZeroDivisionError:
    print('0不能为除数哦')
else:
    print('else')

try:
    print(4 / 1)
finally:
    print('finally')

# try:
#     count = 0
#     if count == 0:
# # raise 'count == 0', count
# except:
#     print('raise')
