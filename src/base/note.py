# coding=utf-8
# 笔记

"""
int 类型的list 转换为 str
"""


def int_list_trans_str():
    print ','.join(str(i) for i in (1, 3, 4, 5, 6))


def test_eval():
    print type(eval('{3,4,5,6,7,8}'))  # set
    print type(eval('[3,4,5,6,7,8]'))  # list
    print type(eval('(3,4,5,6,7,8)'))  # tuple
    print type(eval('2,3,4,6'))  # tuple
    print type(eval('56'))  # int
    print type(eval('56.5'))  # float
    print type(eval('56L'))  # long


def test_dict():
    var = {
        'name': 'jack',
        'age': 34,
        'address': 'US'
    }
    print var
    print var.items()
    print var.fromkeys([3, 4, 5, 6], ['3', '4', '5', '6'])
    for v in var.iteritems():
        print v
    print var.keys()
    var.pop('name')
    print var


def str_reverse(string):
    return string[::-1]


if __name__ == '__main__':
    int_list_trans_str()

    test_eval()
