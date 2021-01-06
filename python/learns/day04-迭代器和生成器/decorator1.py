#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

# 装饰器本质是函数,就是为其他函数添加附加功能
# 原则:不能修改被修饰的函数的源代码及调用方式
# 实现:函数即“变量”;高阶函数;嵌套函数
# 高阶函数:1把一个函数名当做实参传给另一个函数;2返回值中包含函数名

# def foo():
#     print("in the foo")
#     bar()
# foo() # 会报错,没有定义bar()这个函数

# def bar():
#     print("in the bar")
# def foo():
#     print("in the foo")
#     bar()
# foo() # 在调用之前定义函数,能够被调用到


# def foo():
#     print("in the foo")
#     bar()
# foo() # 在调用之后定义函数,不能被调用
# def bar():
#     print("in the bar")


def foo():
    print("in the foo")
    bar()


def bar():
    print("in the bar")


foo()
