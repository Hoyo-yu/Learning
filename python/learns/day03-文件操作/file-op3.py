#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# Modify the content of the file.

"""
f = open("file", 'r', encoding="utf-8")
f_new = open("file.bak", 'w', encoding="utf-8")

# 需要从命令行传递参数

find_str = sys.argv[1]
change_str = sys.argv[2]

for line in f:
    if find_str in line:
        line = line.replace(find_str, change_str)
    f_new.write(line)
f.close()
f_new.close()
"""
# 可以使用with方法来防止忘记文件的关闭,上面的程序可以改写为下面的方式.

with open("file", 'r', encoding="utf-8") as f, \
        open("file.bak", 'w', encoding="utf-8")as f_new:
    for line in f:
        if "抱我" in line:
            line = line.replace("抱我", "baowo")
        f_new.write(line)

