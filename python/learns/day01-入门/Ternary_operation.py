#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

a, b, c = 1, 3, 5
if a < b:
    d = a
else:
    d = c
# 等价于
# d = a if a < b else c
print(d)
