#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

"""
f = open("file", 'r', encoding="utf-8")
data = f.read() # r只读,read()读取文件内所有内容,此时光标在文件末尾
print(data)
f.close()
"""

"""
f = open("file2", 'w', encoding="utf-8")
data = f.write("你好呀！")
f.close()  # w写,打开的文件是已存在的文件,会将原内容清空;打开的是新文件,会将新内容写入到新文件.
"""
# 移动光标位置对文件的写入没有影响

f = open("file", 'a', encoding="utf-8")
f.write("\n你好呀")  # a追加,在末尾追加新内容,不可读;文件不存在就创建
# data = f.read()
# print(data)
f.close()

# '+'与r/w/x/a一同使用，在原功能基础上增加同时读写功能
