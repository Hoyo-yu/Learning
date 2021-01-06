#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3默认使用utf-8
# Author:Mario

import copy

# 列表
names = ["lhy", "zhangsan", "lisi", "wangwu"]

print(names)
print(names[0], names[3])
print(names[1:3])
print(names[:3])
print(names[0: -1])  # 切片
print(names[:-1])
print(names[-2:])
names.append("aaa")
names.insert(1, "ccc")  # 增
names[2] = "ccc"  # 改
print(names)  # 查
names.remove("ccc")  # 删
del names[1]  # names.pop(1)

print(names)
print(names.index("wangwu"))  # 查位置

# names.sort()
# print(names)  # 排序

names[0] = ['ddd', 'eee']
# name2 = names.copy()  # 复制
name2 = copy.copy(names)
# name2 = names[:] # 等价于names=names[0:-1]
# name2 = list(names)
name3 = copy.deepcopy(names)
print(name2)
print(name3)

names[0][0] = 'fff'  # 改names中的一个值,name2相应位置的值并没有改变
print(name2)
print(name3)  # deepcopy会把嵌套的对象完全拷贝并开辟一片空间,成为一个新的对象,完全脱离了names
