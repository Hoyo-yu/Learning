#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

import time


def timer(func):
    def deco(*args, **kwargs):  # 符合装饰器的条件1:嵌套函数
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("the func run time is %s" % (stop_time - start_time))

    # 返回的是deco函数的内存地址
    return deco  # 符合装饰器的条件2:高阶函数


@timer  # test1=timer(test1),哪个函数需要这个装饰器直接在这个函数前使用 @装饰器函数名
def test1(name, age):
    time.sleep(1)
    print("in the test1")
    print("name:%s,age:%d" % (name, age))


# test1 = timer(test1)  # timer调用的是函数test1的内存地址
# 没有改变原来函数的源代码,但是新增了打印函数运行时间的功能
test1("lhy", 24)
