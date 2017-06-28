# coding=utf-8

# 2的3次方
print 2 ** 3
# 取整
print 2 // 3
# <> 不等于 相当于!=
list = [2, 3, 4]
list_back_up = [2, 3, 4, 5]
print list != list_back_up
# 位运算
a = 60  # 0011 1100
b = 13  # 0000 1101

print a & b  # 12  0000 1100 都是1得1,否则为0
print a | b  # 61  0011 1101 有一个1则得1,否则为0
print a ^ b  # 49  0011 0001 对应的二进位不同时得1,否则为0
print ~a  # -61  1100 0011 对每个二进位取反,0换为1,1换为0
print a << 2  # 240 1111 0000 各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0
print a >> 2  # 15 0000 1111 把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数

# 逻辑运算符
# and 相当于java中的&&
# or 相当于java中的||
# not 相当于java中的!(),其实就是取反


# 成员运算符
'''
n	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
'''
inList = [1, 2, 3, 4, 5]
print 3 in inList  # True
print 12 in inList  # False

# 身份运算符

'''
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
'''

# is 相当于java中的equals, is not 相当于java中的 !equals

aa = '12'
bb = '12'
cc = '23'
print aa is bb
bb = '34'
print aa is bb
print aa is cc

# is 和 == 区别 (相当于 java中的 equals 和 == )

#  运算符优先级
'''
**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，取模和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
<> == !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
'''
