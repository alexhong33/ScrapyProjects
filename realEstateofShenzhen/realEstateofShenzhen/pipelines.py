# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql



class RealestateofshenzhenPipeline(object):
    
  
    def process_item(self, item, spider):
        
        dbconn = pymysql.connect(host="localhost", 
                                    user="root", 
                                    passwd="admin",
                                    db="realestateofshenzhen",
                                    charset = "utf8")

        
        for j in range(0, len(item["ResidentalName"])):
            
            ResidentalName = item["ResidentalName"][j]
            District = item["District"][j]
            Area = item["Area"][j]
            Space = item["Space"][j]
            Structure = item["Structure"][j]
            PricePerSquareMeter = item["PricePerSquareMeter"][j]
            TotalPrice = item["TotalPrice"][j]
            DetailedAddress = item["DetailedAddress"][j]
            Url = item["Url"][j]
            
            
            # 构造sql语句
            sql = "insert into house_shenzhen(ResidentalName, \
            District, Area, Space, Structure, PricePerSquareMeter, \
            TotalPrice, DetailedAddress, Url) VALUES( \
            '"+ResidentalName+"','"+District+"','"+Area+"','"+Space+"', \
            '"+Structure+"','"+PricePerSquareMeter+"','"+TotalPrice+"', \
            '"+DetailedAddress+"', '"+Url+"')"
            
            # 通过query实现执行对应的sql语句
            
            dbconn.query(sql)
         
        return item
    
def close_spider(self, spider):
    self.dbconn.close() 
        
