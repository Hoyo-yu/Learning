#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
import time


def consumer(name):
    print("%s准备吃包子了" % name)
    while True:
        baozi = yield
        print("包子%s来了，被%s吃了一半" % (baozi, name))


# c = consumer("lhy")
# print(c.__next__())
# bz1 = "韭菜馅"
# c.send(bz1)
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()  # 走到baozi=yield这一步,不会打印print("%s准备吃包子了" % name)
    c2.__next__()
    print("我开始做包子了")
    for i in range(1, 10):
        time.sleep(1)
        print("做了一个包子")
        c.send(i)
        c2.send(i)


producer("lhy")
