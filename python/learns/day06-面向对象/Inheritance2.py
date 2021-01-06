#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 在python3中经典类和新式类都是按广度类优先来继承的
# 在python2中经典类是按深度优先来继承的,新式类是按广度类优先来继承的

class A(object):
    def __init__(self):
        print("A")


class B(A):
    pass
    # def __init__(self):
    #     print("B")


class C(A):
    pass
    # def __init__(self):
    #     print("C")


class D(B, C):
    pass
    # def __init__(self):
    #     print("D")


obj = D()  # 只使用一个构造函数,顺序是从下到上,从左到右,也就是B->C->A的顺序,如果某个继承的类里有构造函数就停止向后找了
# 此处的D是继承B、C的,而B、C是继承A的,这种查找方式叫"广度优先"：D->B->C->A,往后顺延
# 还有另外一种查找方式叫"深度优先":D->B->A->C,往后顺延
