#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

list1 = [1, 4, 5, 7, 4, 2, 9]
list1 = set(list1)
list2 = set([2, 3, 6, 5, 7, 8])
list3 = set([5])

print(list1, type(list1))
print(list2, type(list2))
print(list1.intersection(list2))  # 交集
# print(list1 & list2)
print(list1.union(list2))  # 并集
# print(list1 | list2)
print(list1.difference(list2))  # 差集
# print(list1 - list2)
print(list2.difference(list1))  # 差集
# print(list2 - list1)
print(list3.issubset(list2))  # 判断前者是否是后者的子集
print(list1.issuperset(list3))  # 判断前者是否是后者的夫集
print(list1.symmetric_difference(list2))  # 对称差集
# print(list1 ^ list2)

list4 = set([])
list4.add(1)  # 添加一个元素
list4.update([1, 2, 3])  # 更新集合
print(list4)
list4.remove(1)  # 删除一个元素,不存在的元素会报错
list4.discard(1)  # 删除一个元素，不存在的元素不会报错
list4.pop()  # 任意删除一个元素,返回删除的元素

len(list1)  # 集合的长度
