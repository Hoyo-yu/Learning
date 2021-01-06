#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

with open("test.txt", 'r', encoding="gbk") as f, \
        open("test.bak", 'w', encoding="utf-8")as f_new:
    for line in f:
        f_new.write(line)

# 将gbk文件格式转换成utf-8文件格式
