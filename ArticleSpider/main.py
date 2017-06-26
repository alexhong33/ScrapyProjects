# -*- coding: utf-8 -*-
# @Time        : 2017/6/26 15:08
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : main.py
# @Description : STOP wishing START doing

from scrapy.cmdline import execute

import sys
import os

# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])

 