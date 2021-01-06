#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 杨辉三角
L = [1, 2, 3]
print(len(L))
print(range(len(L)))


# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         # L = [L[i - 1] + L[i] for i in range(len(L))]
#         new_L = []
#         for i in range(len(L)):
#             new_L.append(L[i - 1] + L[i])
#         L = new_L
def triangles():
    l = [1]
    while True:
        yield l
        l = [0]+l+[0]
        l = [l[i]+l[i+1] for i in range(len(l)-1)]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
