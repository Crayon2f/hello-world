# coding=utf-8

import random_
#
# s = int(random.uniform(1, 10))
# # print(s)
# m = int(input('输入整数:'))
# while m != s:
#     if m > s:
#         print('大了')
#         m = int(input('输入整数:'))
#     if m < s:
#         print('小了')
#         m = int(input('输入整数:'))
#     if m == s:
#         print('OK')
#         break

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# odd = []
# even = []
#
# while len(numbers) > 0:
#     number = numbers.pop()
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
# print odd, even

# 猜拳游戏
gameMap = {
    1: '石头',
    2: '剪刀',
    3: '布'
}
while True:
    computerKey = int(random_.uniform(1, 4))
    computerValue = gameMap[computerKey]
    m = raw_input('输入 石头、剪子、布,输入"end"结束游戏:')
    keyList = gameMap.values()
    if m not in keyList and m != 'end':
        print '输入不对'
    elif m == 'end':
        print '退出游戏...'
        break
    else:
        if m == computerValue:
            print '平局'
        elif (m == '石头' and computerValue == '剪刀') or (m == '布' and computerValue == '石头') or (m == '剪刀' and computerValue == '布'):
            print 'you win !'
        else:
            print 'you lose !'


