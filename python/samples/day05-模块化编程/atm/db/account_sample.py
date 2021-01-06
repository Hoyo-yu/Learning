#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario


import json

acc_dic = {
    # 初识账户信息
    'id': "admin",
    'password': 'admin',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0  # 0 = normal, 1 = locked, 2 = disabled
}

print(json.dumps(acc_dic))
