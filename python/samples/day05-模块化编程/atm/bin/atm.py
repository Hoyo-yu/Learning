#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from core import main
# from core.main import A

if __name__ == '__main__':
    main.run()
    # a = A("Mario")
    # a.print_name()
