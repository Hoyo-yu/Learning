#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 类方法:只能访问类变量,不能访问实例变量
class Dog(object):
    n = "Mario"

    def __init__(self, name):
        self.name = name
        # self.n = "Mario"  # 会报错

    @classmethod
    def eat(self):
        print("%s is eatting %s" % (self.n, "cake"))


d = Dog("Mario")
d.eat()
