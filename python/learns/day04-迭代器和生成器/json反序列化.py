#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# json用于不同语言之间的交互,与xml类似
# import json
#
# f = open("test.txt", 'r')
# # data = eval(f.read())
# data = json.loads(f.read())
# print(data)
# f.close()
# print(data["name"])
import pickle


def hello(name):
    print("hello", name)
    print("hello2", name)


print(hello)  # 与序列化的hello内存地址不一样,两个程序内的相同函数名的函数内存地址是不一样的
f = open("test.txt", 'rb')
# data = eval(f.read())
data = pickle.load(f)  # data = pickle.loads(f.read())
# 建议写程序时只dump(s)一次,只load(s)一次
print(data)
f.close()
print(data["func"]("Mario"))
