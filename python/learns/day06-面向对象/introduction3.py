#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

# 析构函数:在实例释放或销毁的时候自动执行,通常用于做一些收尾工作,如关闭一些数据库连接、关闭打开的临时文件等
class dog(object):  # 继承object类

    def __init__(self, name):  # 构造函数
        self.name = name  # 静态属性

    def __del__(self):  # 析构函数
        print("%s很不幸的死掉了" % self.name)

    def bark(self):  # 类的方法(动态属性)
        print("%s:汪汪汪" % self.name)

    def __sceret(self):  # 私有方法
        print("Everyone has his own secret, so does the dog.")


d1 = dog("xx")  # 析构函数在程序结束时调用
d2 = dog("yy")
d1.bark()
del d2  # 析构函数在实例销毁时立即调用
