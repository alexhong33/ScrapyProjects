# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestateofshenzhenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 住宅名
    ResidentalName = scrapy.Field()
    # 辖区
    District = scrapy.Field()
    # 位置
    Area = scrapy.Field()
    # 面积
    Space = scrapy.Field()
    # 户型
    Structure = scrapy.Field()
    # 每平方价格
    PricePerSquareMeter = scrapy.Field()
    # 总价
    TotalPrice = scrapy.Field()
    # 详细地址
    DetailedAddress = scrapy.Field()
    # 链接
    Url = scrapy.Field()
