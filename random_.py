# coding=utf-8
# 随机函数

"""
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

"""
import random

collection = [1, 2, 3, 4, 5, 6, 7, 8]

print random.choice(collection)

print random.randrange(2, 10)

print random.seed(10)

random.shuffle(collection)
print collection

random.shuffle(collection)
print collection

print random.uniform(3, 10)
