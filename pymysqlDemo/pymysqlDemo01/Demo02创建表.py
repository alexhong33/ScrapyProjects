'''
Created on 2017年6月16日

@author: Alex
'''

import pymysql

# 通过db参数, 连接到指定数据库 myfirstpydb
conn = pymysql.connect(host="localhost", user="root", passwd="admin", db="myfirstpydb")
'''
 在数据库下 创建了一个名为 mytb的表
其中有两个字段
第一个字段为title 用来存储文章标题
第二个字段为keyword 用来存储当前页面的关键字

'''
#conn.query("CREATE TABLE mytb(title CHAR(20) NOT NULL, keyword CHAR(30))")

# 通过python代码试着向mytb表中插入一些数据
conn.query("INSERT INTO mytb(title, keyword) VALUES('first title', 'first keyword')")

conn.commit()
conn.close()