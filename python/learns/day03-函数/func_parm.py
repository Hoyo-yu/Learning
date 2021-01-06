#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 形参和实参

def test1(x, y, z):
    print(x, y, z)


a = 1
b = 2
c = 3
test1(1, 2, 3)  # 形参和实参一一对应,位置参数调用
test1(x=a, y=b, z=c)
test1(y=1, x=2, z=6)  # 关键字调用
test1(3, z=6, y=2)  # 关键字参数在位置参数后


# test(2, y=3,6)


def test2(x, y=2):
    print(x, y)


test2(1, 3)  # 调用参数时,默认参数非必须传递
test2(1)
