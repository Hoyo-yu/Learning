#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 可以直接作用于for循环的数据结构有:list,tuple,dict,set,str,generator和带yield的generator function
# 可迭代对象(Iterable):这些可以直接作用于for的对象称为可迭代对象
# 迭代器(Iterator):可以被next()函数调用并不断返回下一个值的对象称为迭代器
# 查看可调用的方法dir()
# from collections.abc import Iterable  # 判断是否为可迭代对象
#
# print(isinstance([], Iterable))
# print(isinstance((), Iterable))
# print(isinstance({}, Iterable))
# print(isinstance(set(), Iterable))
# print(isinstance('abc', Iterable))
# print(isinstance((x for x in range(10)), Iterable))

from collections.abc import Iterator  # 判断是否为迭代器对象

print(isinstance(iter([]), Iterator))  # 可以使用iter()方法是使其他的Iterable变成Iterator
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance(set(), Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
