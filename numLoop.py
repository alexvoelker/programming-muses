#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
# -*- coding: utf-8 -*-

import random

count = 0
while count <= 10000000000:
    num = random.randint(0, 10)
    print(num, end="")
    count += 1
    
