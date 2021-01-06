#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# import json  # 简单的序列化
#
# info = {
#     "name": "Mario",
#     "age": "24"
# }
# f = open("test.txt", 'w')
# # f.write(str(info))
# print(json.dumps(info))
# f.write(json.dumps(info))
# f.close()
import pickle  # 简单的序列化


def hello(name):
    print("hello", name)


print(hello)
info = {
    "name": "Mario",
    "age": "24",
    "func": hello
}
f = open("test.txt", 'wb')
# f.write(str(info))
print(pickle.dumps(info))
pickle.dump(info, f)  # f.write(pickle.dumps(info))
f.close()
