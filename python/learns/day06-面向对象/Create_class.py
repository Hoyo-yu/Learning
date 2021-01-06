#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 创建类的两种方式
class Foo(object):  # 普通方式
    def func(self):
        print("Hello World")


f = Foo()
f.func()


def func2(self):
    print("Hello %s " % self.name)


def __init__(self, name, age):
    self.name = name
    self.age = age


Foo2 = type('Foo', (object,), {"func2": func2, "__init__": __init__})
# Foo2既是类也是对象,f2为Foo2的实例对象;Foo2也是type这个类实例化产生的对象
f2 = Foo2("Mario", 22)
f2.func2()
print(type(Foo2))
