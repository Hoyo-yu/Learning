#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
import time


def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open("data", "a+") as f:
        f.write("%s end action\n" % time_current)


def test1():
    print("in the test1")
    logger()


def test2():
    print("in the test1")
    logger()


def test3():
    print("in the test1")
    logger()


test1()
test2()
test3()
