# coding=utf-8

# for循环
print('------------------ for ------------------------')
fruits = ['apple', 'banana', 'mango']

for fruit in fruits:
    print(fruit)

for index in range(len(fruits)):
    print(index)
print('-------------- for else ------------------')
numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    if number % 2 == 0:
        print(number)
        break
else:
    print('else')

print('------------------ enumerate ------------------------')
for index, item in enumerate(fruits):
    print(index, item)

primeList = []

for num in range(2, 100):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primeList.append(num)
print(primeList, len(primeList))

if 4 % 2:
    print('----- 4%2=0 在if条件判断中是false(只有为0时候是false) -----------')
elif 4 % 3:
    print('------ 4%3=1 在if条件判断中是true---------')
