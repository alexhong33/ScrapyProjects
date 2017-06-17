'''
Created on 2017年6月16日

@author: Alex
'''

import pymysql
from twisted.conch.insults.window import cursor

conn = pymysql.connect(host="localhost", user="root", passwd="admin", db="myfirstpydb")

cursor = conn.cursor()
sql = "select * from mytb"
cursor.execute(sql)

for i in cursor:
    print("当前是第"+str(cursor.rownumber)+"行")
    print("标题是: "+i[0])
    print("关键词是: "+i[1])