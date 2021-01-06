#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 将源码根目录添加到系统的环境变量,将根目录设置到需要调用的模块的上上级目录
# 比如需要掉用mod_b下面的bbb模块,需要将根目录设为mod_b目录的上级目录"软件目录结构规范"
sys.path.append(path)
from mod_b.bbb import B


class A(object):
    def print_A(self):
        print("A")


b = B()
b.print_B()
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
