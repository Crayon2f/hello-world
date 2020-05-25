# coding=utf-8
def __private_method():
    print('this is a private method')


def public_method():
    print('this is a public method')


class Person:
    """定义人的类"""
    age = 0
    # 私有变量 以"__"开头
    __girlFriend = 'rose'

    def __init__(self, name, address):
        Person.age = 23
        self.name = name
        self.address = address

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, 'destroy')

    def getGirlFriend(self):
        return self.__girlFriend

    def setGirlFriend(self, __girl_friend):
        self.__girlFriend = __girl_friend

    @staticmethod
    def static_method():
        print('this is a static method')


person = Person('jack', '美国')

person.setGirlFriend('肉丝儿')
print(person.address, person.age, person.name, person.getGirlFriend())

public_method()
Person.static_method()

p1 = Person('hello', 'beijing')
p2 = p1
p3 = p1
print(id(p1), id(p2), id(p3))
del p1  # 析构函数 __del__ ，__del__在对象消逝的时候被调用，当对象不再被使用时，__del__方法运行：
del p2

# print(Person.__doc__)
# print(Person.__name__)
# print(Person.__module__)
# print(Person.__bases__)
# print(Person.__dict__)
