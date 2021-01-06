#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
from mod_b.bbb import B

# 该文件调用同级目录下的文件夹内的文件(模块)可以直接使用mod_b.bbb,在此之前要利用__init__.py将文件夹变成模块
b = B()
b.print_B()
