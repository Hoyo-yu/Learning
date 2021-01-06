#!/usr/bin/env python
# -*- coding: utf-8 -*-
# dict是无序的,key-value,key是唯一的

# 字典的嵌套
movie = {
    "USA": {
        "Scent of a Woman": [9.2, "it is very good!"]
    },
    "CHN": {
        "Dying to Survive": [8.8, "Moved to tears."]
    }
}
movie.setdefault("UK", {"xxx": [4.0, "it is terrible"]})
print(movie)  # 如果之前字典中不存在这个键，添加新的key-value
movie.setdefault("CHN", {"xxx": [4.0, "it is terrible"]})
print(movie)  # 如果之前字典中存在这个键,返回原键值

info = {
    'stu1101': 'liuhuyao',
    'stu1102': 'zhangsan',
    'stu1103': 'lisi',
}
info2 = {
    'stu1101': 'lhy',
    1: 2,
    2: 3,

}
# 字典的增删改查
print(info['stu1101'])  # 查,事先知道他有这个键
# print(info.get('stu1101'))# 建议使用
# print('stu1101' in info)  python2.x中等同于info.has_key("stu1101")

info['stu1101'] = 'lhy'  # 改
print(info)

info['stu1104'] = 'wangwu'  # 增
print(info)

del info['stu1101']
# info.pop('stu1101')
# info.popitem()  随机删除
print(info)

# 字典的基本方法
print(info.values())  # 打印所有键的值
print(info.keys())  # 打印所有的键

info.update(info2)
print(info)  # 把两个字典合并,有相同键不同值就更新,其他就添加

print(info.items())  # 把字典转成列表

# 初始化字典
info3 = dict.fromkeys([1, 2, 3], "test")  # 针对一层有效
print(info3)
info3[1] = '1'
print(info3)

info4 = dict.fromkeys([1, 2, 3], [1, {'name': 'lhy'}, 222])
info4[1][1]["name"] = "liuhuyao"
print(info4)  # 每个键的值都被替换了

# 字典的循环
for i in info:
    print(i, info[i])  # 更高效,建议使用
# for k, v in info.items():
# print(k, v)
