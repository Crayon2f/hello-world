# coding=utf-8

# 函数

def firstFunction():
    """第一个函数"""
    print 'my first function'
    return


firstFunction()

lst = [1, '23', 'aaa']


def changeList(paramList):
    if paramList is not None:
        paramList.extend([5, 6, 7])
    return


print 'pre : ', lst
changeList(lst)

print 'after : ', lst


def defaultParam(name, age=23):
    """ 参数默认值 """
    print 'name:', name, '-----', 'age:', age


defaultParam('java', 45)
defaultParam('javascript')


def variableParam(param1, param2, *params):
    """ 可变参数 params是一个元祖,存放的是除去(params之前的参数)"""
    print 'param1', param1
    print 'param2', param2
    print 'params', params
    # for param in params:
    #     print param
    return


variableParam(34, 15)
variableParam('ddd', 'eee', 23)

lambdaFunction = lambda x, y, z: x + y * z  # lambda 表达式

print lambdaFunction(3, 4, 5)

count = 3

print 'pre - ', count
def scope():
    """ 作用域 """
    count = 23 + 45
    print 'scope - ', count
    return count
# count = scope()
print 'after - ', count


