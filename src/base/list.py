# coding=utf-8

# list
import itertools

temp_list = [12]
temp_list2 = [234]
# print(int('abc'))
# print(cmp(temp_list, temp_list2))

list2 = ['a', 'b', 'c', 'd', 'e']

print(list2[0])
list2[0] = 12

print(list2[0])

for var in range(len(list2)):
    if var == 2:
        del list2[var]
print(list2)
print('----------------------------------')
lst = [12, 34, 556, 76, 78]

lst2 = [34, 55, 6, 7]

print(lst + lst2)
print('----------------------------------')
print(len(lst))
print('----------------------------------')
print(34 in lst)
print('----------------------------------')
print(lst[-2])
print('----------------------------------')
print(lst[1:])
print('----------------------------------')
print(max(lst))
print(min(lst))
print((lst + lst2).count(34))
print(lst.index(34))
print('----------------------------------')
lst.append(123)
print(lst)
print('----------------------------------')
lst.insert(2, 444)
print(lst)
print('----------------------------------')
print(lst.pop(2))
print(lst)
print('----------------------------------')
lst.sort()
print(lst)
print('----------------------------------')
lst.reverse()
print(lst)
print('----------------------------------')
print(lst)
print(lst2)
lst.extend(lst2)
print(lst)
print('----------------------------------')

# ####### list去重
lst3 = lst + lst2
print(lst3)
lst3 = set(lst3)
print(list(lst3))
print('----------------------------------')
ids = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
ids.sort()
it = itertools.groupby(ids)
for k, g in it:
    print(k)
print('----------------------------------')
newList = []
print(lst + lst2)
for i in (lst + lst2):
    if i in newList:
        continue
    else:
        newList.append(i)
print(newList)
