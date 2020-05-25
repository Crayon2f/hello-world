# coding=utf-8

class Parent:
    parentAttr = 100

    def __init__(self):
        print('parent__init__')

    def parentMethod(self):
        print(self.parentAttr)


class Child(Parent):
    print
