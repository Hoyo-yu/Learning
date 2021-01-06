#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 属性方法:把一个方法变成一个静态属性
class Dog(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eatting %s" % (self.name, self.__food))

    @eat.setter
    def eat(self, food):
        print("set to send", food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("已删除")


d = Dog("Mario")
d.eat
d.eat = "cake"
d.eat
del d.eat

