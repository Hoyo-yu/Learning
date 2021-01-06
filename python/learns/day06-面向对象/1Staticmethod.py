#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 静态方法:只是名义上归"类"管理,实际上在静态方法里访问不了类或实例中的任何属性
class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod  # 就是类下面的一个函数,实际上跟类没什么太大关系
    def eat():
        print("%s is eatting %s" % ("lhy", "cake"))

    def eatting(obj):
        print("%s is eatting" % obj.name)

    def talk(self):
        print("%s is talking" % self.name)


Dog.eat()
d = Dog("Mario")
Dog.eatting(d)
d.talk()
#ssss