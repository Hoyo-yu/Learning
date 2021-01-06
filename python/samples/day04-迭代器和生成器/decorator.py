#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

user, passwd = "Mario", "abc123"


def auto(func):
    def wrapper(*args, **kwargs):
        username = input("username:").strip()
        password = input("password:").strip()
        if user == username and passwd == password:
            print("\033[32;1mUser has passed authentication\033[0m")
            res = func(*args, **kwargs)
            return res
        else:
            exit("\033[31;1mInvalid username or password\033[0m")

    return wrapper


def index():
    print("welcome to index page")


@auto
def home():
    print("welcome to home page")
    return "From home"


@auto
def bbs():
    print("welcome to bbs page")


index()
print(home())
bbs()
