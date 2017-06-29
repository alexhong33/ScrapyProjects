# -*- coding: utf-8 -*-
# @Time        : 2017/6/29 17:09
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : zhihu_login_requests.py
# @Description : STOP wishing START doing. 

import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"
header = {
            "HOST": "www.zhihu.com",
           # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           #"Accepting-Encoding": "gzip, deflate, br",
           #"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "User-Agent": agent,
           #"Connection": "keep-alive",
           "referer": "https://www.zhizhu.com"
            }

def get_xsrf():
    response = requests.get("https://www.zhihu.com", headers = header)
    # 默认header是python2, python3
    #response = requests.get("https://www.zhihu.com")
    print (response.text)
    return ""


def zhihu_login(account, password):
    #知乎登录
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf" : "",
            "phone_num" : account,
            "password" : password
        }