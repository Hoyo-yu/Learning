#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

import getpass

_username = 'lhy'
_password = '123456'

username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")
# print(username, password)

if _username == username and _password == password:
    print("welcome user {name} login".format(name=username))
else:
    print("username error or password error")
print("lhy")
