#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
def foo():
    print("in the foo")

    def bar():
        print("in the bar")
        # 函数的嵌套

    bar()


foo()
