#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from mod_b.mod_a.aaa import A
from mod_b.bbb import B

a = A()
a.print_A()
print(a.__module__)  # 类的特殊成员方法
print(a.__class__)  # 类的特殊成员方法
b = B()
b.print_B()
