# -*- coding: utf-8 -*-
# @Time        : 2017/6/29 17:09
# @Modified    : 2017/7/18 10:07
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

session = requests.session()

# 对cookie加载
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未能加载")

agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"
header = {"HOST":"www.zhihu.com","Referer":"https://www.zhihu.com/", "User-Agent":agent}

def is_login():
    # 通过个人中心页面返回状态码来判断是否为登录状态
    inbox_url = "https://www.zhihu.com/inbox"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True

# 获取xrsf码
def get_xsrf():
    # 获取xsrf_code
    response = session.get("https://www.zhihu.com/", headers = header)

    # 默认header是python2, python3
    # response = requests.get("https://www.zhihu.com")
    # print(response.text)
    # text = '<input type="hidden" name="_xsrf" value="689f30beb44d8c05753c1d187b810c9d"/>'
    t = response.text
    match_obj = re.search('.*name="_xsrf" value="(.*?)"', t)
    if match_obj:
        print(match_obj.group(1))
    else:
        return ""


# 打印登录持久化页面
def get_index():
    response = session.get("https://www.zhihu.com/", headers=header)
    with open("index_page.html", "wb") as f:
        f.write(response.text.encode("utf-8"))
    print("ok")



def zhihu_login(account, password):
    #知乎登录
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf" : get_xsrf(),
            "phone_num" : account,
            "password" : password
        }
    else:
        if "@" in account:
            # 判断用户名是否为邮箱
            print("邮箱方式登录登录")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": get_xsrf(),
                "email": account,
                "password": password
            }
    response_text = session.post(post_url, data=post_data, headers=header)
    session.cookies.save()


# zhihu_login("13723728569", "Shenzhen2017")
# get_index()
is_login()