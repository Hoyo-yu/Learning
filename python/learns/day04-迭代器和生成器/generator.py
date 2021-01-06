#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 生成器:只有调用时才会生成相应的数据,只记录当前位置,只有一个__next__()方法,省内存
# 列表生成式:[i*2 for i in range(1000)]
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"


for i in fib(6):
    print(i)
# while True:
#     try:
#         x = next(f)
#         print(x)  # f.__next__()=next(f)
#     except StopIteration as e:
#         print("Generator return value", e.value)
#         break
