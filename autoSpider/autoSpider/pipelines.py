# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import codecs
import json
from nt import link
from scrapy import item



class AutospiderPipeline(object):
    
    def __init__(self):
        # 打开mydata.json文件
        self.file = codecs.open("F:/PythonDownload/autoSpider/mydataFormatting.json", "wb", encoding="utf-8")
    
    def process_item(self, item, spider):
        
        '''
                        版本一
                        
        i = json.dumps(dict(item), ensure_ascii=False)
        # 每条数据后加上换行
        line = i + '\n'
        # 数据写入到mydata.json文件中
        self.file.write(line)
        
        return item
        
        '''
        
        # item = dict(item)
        # print(len(item["name"]))
        
        # 每一页中包含多个商品信息, 所以可以通过循环, 每一次处理一个商品
        # 其中 len(item["name"]) 为当前页中商品的总数, 依次遍历
        
        for j in range(0, len(item["name"])):
            
            # 将当前页的第j个商品的名称赋值给变量name
            name = item["name"][j]
            price = item["price"][j]
            comnum = item["comnum"][j]
            link = item["link"][j]
            
            # 将当前页下第j个商品的name, price, comnum, link等信息处理一下
            # 重新组合成一个字典
            
            goods = {"name":name, "price":price, "comnum":comnum, "link":link}
            
            # 将组合后的当前页中第j个商品的数据写入json文件
            i = json.dumps(dict(goods), ensure_ascii = False)
            line = i + '\n'
            self.file.write(line)
            
        # 返回item
        return item
    
        
    def close_spider(self, spider):
        # 关闭mydata.json文件
        self.file.close()