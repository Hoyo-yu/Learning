#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

import sys

print(sys.getdefaultencoding())
s = u"你好"  # unicode,python3的默认编码
print(s, type(s))
s_gbk = s.encode("gbk")
print(s_gbk, type(s_gbk))
s_utf8 = s.encode("utf-8")
print(s_utf8, type(s_utf8))
s_gb2312 = s.encode("utf-8").decode("utf-8").encode("gb2312")
print(s_gb2312, type(s_gb2312))

# #在python 2中默认编码是 ASCII，而在python 3中默认编码是 unicode
# python本身的默认编码是utf-8,unicode能识别所有字符编码的字符串
# unicode 中英文字符均占两个字节,ASCII 英文字符占一个字节
# utf-8(可变长的字符编码)中文字符占3个字节,英文字符占一个字节
# GBK 中文占两个字节,英文占一个字节
