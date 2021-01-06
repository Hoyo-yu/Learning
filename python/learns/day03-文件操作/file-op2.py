#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

"""
f = open("file", 'r+', encoding="utf-8")
for index, line in enumerate(f.readlines()):  # 列表操作
    if index == 9:
        print("------我是分隔符------")
    print(line.strip())  # 把某一行内容进行替换
f.close()
"""

"""
f = open("file", 'r+', encoding="utf-8")
count = 0
for line in f:
    if count == 8:
        print("----我是分隔符----")
        count += 1
        continue
    print(line.strip())
    count += 1
f.close()
"""

f = open("file", 'r+', encoding="utf-8")
print(f.tell())
print(f.readline())
print(f.tell())  # 查看光标的位置
f.seek(0)  # 将光标回到某一位置
print(f.tell())

print(f.encoding)  # 文件的编码
print(f.readable())  # 判断文件是否可读
print(f.seekable())  # 判断光标是否可以移动
f.close()

f1 = open("file2", 'r+', encoding="utf-8")
f1.write('How are you!\n')
f1.write('I am fine.\n')
# f1.truncate(10)  # 从开始位置截断,移动光标位置不会对截断产生影响
f1.close()

"""
f = open("file2", 'wb')  # 文件以二进制编码的方式进行写入.
f.write("I am fine\n".encode())
f.close()
"""
