# coding=utf-8
# 字典,其实就是json,key不可以重复,并且key无序

dict1 = {
    'a': 1,
    'b': 2,
    2: '344',
    34.4: '33'
}
print(dict1)

print('344' in dict1)

print(dict1.has_key('a'))

# del dict1['a']  # 删除键是'Name'的条目
# dict1.clear()  # 清空词典所有条目
# del dict1  # 删除词典

print(len(dict1))

print(str(dict1))

dict2 = dict1.copy()
print(dict2)

print(dict1.fromkeys((5, 4, 5), '55'))  # 构建字典,fromkeys,key

dict3 = dict2.fromkeys((2, 3, 4), '45')

print(dict3)
