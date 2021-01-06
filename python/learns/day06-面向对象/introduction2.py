#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

class Student(object):
    def __init__(self, name, score):
        self.__name = name  # 私有变量(私有属性)只有内部可以访问,外部不能访问
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:  # 增加访问限制
            self.__score = score
        else:
            raise ValueError("bad score")

    def get_grade(self):
        if self.__score >= 90:
            print('A')
        elif self.__score >= 60:
            print('B')
        else:
            print('C')


std1 = Student("lhy", 88)
std1.get_grade()
std1.set_score(92)
std1.get_grade()
print(std1._Student__name)  # 如果需要访问内部的私有变量,python解释器对外把__name变量改成了_Student__name,可以使用_Student__name
# 不建议使用这种方式,因为不同版本的python解释器会把__name改成不同的变量名
std1.__name = "Mario"  # 私有变量下不适用
print(std1.get_name())  # 在外面重新设置私有变量__name不会生效
