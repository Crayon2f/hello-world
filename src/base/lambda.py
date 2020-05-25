# coding=utf-8
# lambda 表达式

lambda_method = lambda x: x + 2

print(lambda_method(23))

listStr = '1234567890'
lst = list(listStr)
intLst = []
for l in lst:
    intLst.append(int(l))

print(intLst)

print(filter(lambda ll: ll % 3 == 0, intLst))

print(map(lambda lll: lll + 3, intLst))

# print(reduce(lambda x, y: x + y, intLst))  # 等同于 sum函数

print(sum(intLst))


def genSquares(n):
    for i in range(n):
        yield i ** 2


print(__name__)

if __name__ == '__main__':
    for i in genSquares(5):
        print(i)
