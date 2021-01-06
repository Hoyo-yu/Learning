#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

"""
import sys
print(sys.path)  # 打印环境变量
print(sys.argv)
print(sys.argv[2])
"""
import os

# cmd_res = os.system("dir")  # 输出到屏幕,不会对结果赋值
# print("----->", cmd_res)  # 命令执行成功,结果为0

cmd_res = os.popen("dir")
cmd_res = os.popen("dir").read()
print("----->", cmd_res)
# os.mkdir("new_dir")
# 如果想调用自己写的模块,可以将自己写的模块放到系统库目录下

# PyCodeObject是python编译器真正编译的结果,python程序运行时,编译的结果保存在内存中的PyCodeObject中
# 运行结束时python解释器将PyCodeObject写回到.pyc文件中,第二次运行时会现在磁盘中寻找pyc文件
