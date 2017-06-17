'''
Created on 2017年6月16日

@author: Alex
'''

import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="admin")
#创建数据库, 并在MYSQL终端通过show databases;查看结果
conn.query("create database myfirstpydb")

