#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 绝对路径:从根目录为起点到你所在的目录
# 相对路径:从一个目录为起点到你所在的目录
import os
import sys

print(__file__)  # 相对路径
print(os.path.abspath(__file__))  # 绝对路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)  # 导入系统环境变量
from core import main

main.login()
