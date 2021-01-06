#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

question = "what your name ? My name is {name}."
print(question.count('a'))  # 字符串中某一字符的数量
print(question.capitalize())  # 首字母大写
print(question.lower())  # 全部小写
print(question.upper())  # 全部大写

print(question.center(50, '-'))  # 不够数量的字符的两侧用某字符代替
print(question.ljust(50, '*'))  # 不够数量的字符的右侧用某字符代替
print(question.rjust(50, '*'))  # 不够数量的字符的左侧用某字符代替

print(question.endswith("?"))  # 判断是否以某字符或某段字符结尾,结果是bool值

print(question.find("name"))  # 查找某字符或字符串的索引,字符串可以进行切片操作
print(question[question.find("y"):])  # 从找到的某个索引开始进行切片操作
print(question.index("name"))  # 查找某字符或字符串的索引

print(question.format(name="liuhuyao"))  # 格式化
print(question.format_map({'name': 'liuhuyao'}))  # 用字典的形式进行格式化

print("ab123".isalnum())  # 判断是否是数字和大小写字母(英文字符)的组合
print('abA'.isalpha())  # 判断是否为纯大小写字母(英文字符)

print('0x13f'.isdecimal())  # 判断是否为数字
# print('123'.isdecimal())
print("1bytes".isdigit())  # byte数字也适合
print("一".isnumeric())  # 汉字数字也符合

print("你好".isidentifier())  # 判断是否是一个合法的标识符
print('a aa'.islower())  # 判断每个字符是否都是小写字母
print(' '.isspace())  # 判断是否为一个空格
print("My Name Is".istitle())  # 判断是否为一个标题(每个首字母大写)

print(''.join(['1', '2', '3']))  # 可以用于列表转为字符串
print('+'.join(['1', '2', '3']))
print('alex lil'.split('l'))  # 以某个字符为分割符存放于列表中,默认为空格

p = str.maketrans("abcdef", "123456")
print("apple".translate(p))  # 利用p这个类似于中英字典来翻译某个字符串

print('alex li'.replace('l', 'L', 2))  # 替换字符串中某一个字符为另外一个字符(可以设置替换的数量)
print('alex lil'.rfind('l'))  # 从左至右拿最右边一个字符的下标

print("AleesxZ".swapcase())  # 字符全部转换,大变小,小变大
