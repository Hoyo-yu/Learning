#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

age_of_lhy = 24
count = 0

while count < 3:
    # for count in range(3):
    # for i in range(0,10,2)
    guess_age = int(input("guess age:"))
    if guess_age == age_of_lhy:
        print("very good,you got it")
        break
    elif guess_age > age_of_lhy:
        print("you guess bigger")
    else:
        print("you guess smaller")
    count += 1
    if count == 3:
        continue_confirm = input("Do you want to continue ?")
        if continue_confirm != 'n':
            count = 0
# else:
#   print("you tried many times")
