#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 全局变量和局部变量
name1 = "liuhuyao"  # 全局变量


def changname(name):
    global name1
    name1 = "Lhy"
    print("before change", name, name1)
    name = "LHY"  # 局部变量,这个函数就是这个变量的作用域
    print("after name", name)
    age = 24


print("name1 before global =", name1)  # 函数未被执行,此时的name1还是全局变量
name = "lhy"
changname(name)  # 函数执行
print(name)
# print(age)  # 在外面没有定义age,函数内的age调不到
print("name1 after global =", name1)
