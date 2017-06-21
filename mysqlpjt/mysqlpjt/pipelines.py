# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class MysqlpjtPipeline(object):
    
    def __init__(self):
        # 刚开始时 链接对应数据库
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="admin", db="myfirstpydb", charset="utf8")
        
        
    def process_item(self, item, spider):
        # 将获取到的name和keywd分别赋给变量name和变量key
        name = item["name"][0]
        key = item["keywd"][0]
        # 构造对应的sql语句
        sql = "insert into mytb(title, keywd) VALUES(%s,%s)"
        # 通过query实现执行对应的sql语句
        self.conn.query(sql,(name,key))
        return item
    
    def close_spider(self, spider):
        self.conn.close()