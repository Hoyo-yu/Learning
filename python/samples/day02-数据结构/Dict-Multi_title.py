#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

data = {
    "北京": {
        "昌平": {
            "city1": ["1", "2"],
        },
        "朝阳": {
            "city2": ["3", "4"],
        },
        "海淀": {
            "city3": ["5", "6"],
        },
    },
    "江西": {
        "南昌": {
            "city": ["1", "2"],
        },
        "九江": {
            "city2": ["3", "4"],
        },
        "新余": {
            "city3": ["5", "6"],
        },
    },
}
exit_flag = False
while not exit_flag:
    for i in data:
        print(i)

    choice = input("选择输入1>>:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择输入2>>:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择输入3>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t\t", i4)
                        choice4 = input("最后一层，按b返回")
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True
