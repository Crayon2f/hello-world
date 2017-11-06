# coding=utf-8
# 格式化

# 采用预编译的方式
# print "My name is %s, and %d's old." % ('jack', 23)  # My name is jack, and 23's old.

print("%6.3f" % 2.3)

stringDemo = 'hello World'
print stringDemo.capitalize()  # 把字符串的第一个字符大写,其他的均小写

print stringDemo.center(20, 'l')  # 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

print stringDemo.count('l', 3)  # 某个字符在字符串中初出现的次数(参数很灵活:后两个参数可以不传，就是检索真个字符串，第三个参数不传，就是第二个到最后)

print stringDemo.endswith('d')  # True 是否已''结束

print stringDemo.endswith('o', 0, 5)  # True

stringTab = 'test\t123'  # expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
print stringTab
print stringTab.expandtabs()

print stringDemo.find('ll', 4)  # 相当于java中的indexOf

print 'a{},b{},c{}'.format(1, 2, 4)
print 'a{1},b{2},c{1}'.format(1, 2, 4)
print 'a{a},b{b},c{c}'.format(a=1, b=2, c=4)

word = {'two': 2, 'three': 3, 'four': 4}

print 'two{two},three{three},four{four}'.format(**word)

wordList = [2, 3, 4]

print 'two{0[0]},three{0[1]},four{0[2]}'.format(wordList)
# {1[0]}-{0[0]}相当于是一个二维数组,第一个参数指的是,format传入的第几个参数,后一个指的是传入值中的角标
print 'two{1[0]}-{0[0]},three{1[1]}-{0[1]},four{1[2]}-{0[2]}'.format(wordList, wordList)  # two2-2,three3-3,four4-4

isalnum = 'aaa3'
print isalnum.isalnum()  # 至少有一个字符并且所有字符/都是字母或数字则返回 True,否则返回 False
isalnum = 'aaa3---'
print isalnum.isalnum()
isalpha = 'abc123'
print isalpha.isalpha()  # 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
isalpha = 'abc'
print isalpha.isalpha()
