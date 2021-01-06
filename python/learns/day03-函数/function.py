#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

def func1():  # 函数
    """
    函数体
    """
    print("in the func1")
    return 0


def func2():  # 过程
    """
    函数体
    """
    print("in the func2")


def func3():  # 函数
    """
    函数体
    """
    print("in the func1")
    return 1, "hello", ["lhy", "kkk"], {"name": "lhy"}


def func4(*args):  # 过程,*args不能接收关键字参数
    """
    函数体
    """
    print(args)


def func5(x, *args):  # 过程
    """
    函数体
    """
    print(x, args)


def func6(**kwargs):  # 过程
    print(kwargs)  # **kwargs:把N个关键字参数，转换成字典的形式
    # print(kwargs["name"])


def func7(name, **kwargs):
    print(name, kwargs)


def func8(name, age=24, **kwargs):
    print(name, age, kwargs)


def func9(name, age=18, *args, **kwargs):
    print(name, age, args, kwargs)


func1()
func2()
func3()  # 返回到一个元组内
func4(1, "sss", ["a"], {"xxx"})
func4(*[1, 2, 3, 4, 4])  # 返回到一个元组内
# func4(1, 2, 3, 4, 4)  # 返回到一个元组内
func5(1, 2, 3, 4, 5)
func6(name="lhy", age=8, sex="male")
# func6(**{"name": "lhy", "age": 8})
func7("lhy", age=24, sex="male")
func8("lhy", sex="male", hobby="play games")
# func8("lhy", 25, sex="male", hobby="play games")
# func8("lhy", sex="male", hobby="play games", age=25)  # 关键字参数在位置参数后
func9("lhy", sex="male", hobby="play games")
