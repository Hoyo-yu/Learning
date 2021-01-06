#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 多态:一种借口,多种实现,以实现借口的重用
class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass
        # raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Cat(Animal):
    def talk(self):
        print("Meow")


class Dog(Animal):
    def talk(self):
        print("Woof! Woof!")

    def __call__(self, *args, **kwargs):
        print("running call", *args, **kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name


d = Dog("哈哈")
# d.talk()
d(1, 2, 3, [4, 5, 6])
Dog("哈哈")("haha")
c = Cat("囡囡")
print(d)  # 默认是打印类的内存地址,可以使用__str__来修改默认的类的返回值
print(Dog.__dict__)  # 类调用,打印类的所有属性,不包括实例属性
print(d.__dict__)  # 打印所有实例属性,不包括类属性
# c.talk()

Animal.animal_talk(c)
Animal.animal_talk(d)
