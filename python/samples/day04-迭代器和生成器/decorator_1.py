#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

user, passwd = "Mario", "abc123"


def auto(auto_type):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            print("\nauto func:", auto_type)
            if auto_type == "local":
                username = input("username:").strip()
                password = input("password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args, **kwargs)
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auto_type == "ldap":
                print("搞毛线ldap")
                # return func(*args, **kwargs)

        return wrapper

    return out_wrapper


def index():
    print("welcome to index page\n")


@auto(auto_type="local")
def home():
    print("welcome to home page")
    return "From home"


@auto(auto_type="ldap")
def bbs():
    print("\nwelcome to bbs page\n")


index()
print(home())
bbs()
