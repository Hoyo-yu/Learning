#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

name = input("name:")  # 从键盘输入
print(type(name))  # 打印变量类型,默认是字符串
age = int(input("age:"))  # 强制类型转换
print(type(age))
job = input("job:")

# 多行输出
info = """
-----info of %s-----
name:%s
age:%d
job:%s
""" % (name, name, age, job)  # 格式化输出

info2 = """
----info of {_name}----
name:{_name}
age:{_age}
job:{_job}
""".format(
    _name=name,
    _age=age,
    _job=job
)  # 格式化输出

info3 = """
----info of {0}----
name:{0}
age:{1}
job:{2}
""".format(name, age, job)  # 格式化输出,不建议

# print(info)
print(info2)
# print(info3)
# 从windows迁移脚本文件时注意:windows下的文件格式是DOS,而linux下的文件格式是unix
# 需要用:set ff=unix将文件格式进行转换
