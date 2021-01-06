#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

product_list = [
    ('Iphone11', 7800),
    ('watch', 1500),
    ('book', 100),
    ('computer', 4500),
    ('bike', 800),
    ('coffee', 30),
]
shopping_list = []

salary = input("your current money:")
if salary.isdigit():
    salary = int(salary)
    while True:
        # for item in product_list:
        # print(product_list.index(item), item)
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("please choose goods,press 'q' or 'Q' to quit:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if len(product_list) > user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is %s" % (p_item, salary))
                else:
                    print("your current balance %s is poor" % salary)
        elif user_choice == 'q' or user_choice == 'Q':
            print("-------shopping list------")
            for p in shopping_list:
                print(p)
            print("Your current balance:", salary)
            exit()
        else:
            print("Invalid option")
else:
    print("input error")
