#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 递归特性:必须要有一个明确的结束条件,问题规模相比上次应有所减少,效率不高
def clac(n):
    print(n)
    if int(n / 2) > 0:
        return clac(int(n / 2))
    print("---->", n)


clac(10)
