# -*- coding: utf-8 -*-
# @Time        : 2017/6/28 10:48
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : common.py
# @Description : STOP wishing START doing. 

import hashlib

def get_md5(url):
    # 对URL进行检查
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == "__main__":
    print(get_md5("http://jobbole.com".encode('utf-8')))
 