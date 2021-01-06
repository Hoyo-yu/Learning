#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

msg = "我爱北京天安门"
print(msg)
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))
