#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 高阶函数
import time


def bar():
    time.sleep(1)
    print("in the bar")


def test1(func):
    start_time = time.time()
    func()  # run bar
    stop_time = time.time()
    print("the func run time is %s" % (stop_time - start_time))


test1(bar)  # 高阶函数实例1,把一个函数名当做实参传给另一个函数
# def bar():
#     print("in the bar")
#
#
# def test2(func):
#     print(func)
#     return func  # 高阶函数实例2,返回值中包含函数名
#
#
# bar = test2(bar)
# bar()
