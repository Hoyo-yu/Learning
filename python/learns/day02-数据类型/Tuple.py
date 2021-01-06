#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 只读列表,两个方法index()和count()

names = ('zhangsan', 'lisi', 'wangwu')
print(names.count('wangwu'))
print(names.index("lisi"))
names = list(names)
print(names)
