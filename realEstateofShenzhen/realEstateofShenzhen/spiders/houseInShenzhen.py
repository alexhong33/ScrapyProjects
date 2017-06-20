# -*- coding: utf-8 -*-
import scrapy
from realEstateofShenzhen.items import RealestateofshenzhenItem
from scrapy.http import Request


class HouseinshenzhenSpider(scrapy.Spider):
    name = 'houseInShenzhen'
    allowed_domains = ['esf.fangdd.com/shenzhen']
    # 3 代表 福田区
    dst = "3"
    
    def start_requests(self):
        # 首次爬取模拟成浏览器
        yield Request("http://esf.fangdd.com/shenzhen/list/s134"+str(self.dst), headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400"})

    def parse(self, response):
        item = RealestateofshenzhenItem()
        item["ResidentalName"] = response.xpath("//span[@class='name']/text()").extract()
        
        
        item["District"] = response.xpath("//div[@class='detail']/span[1]/a/text()").extract()
        item["Area"] = response.xpath("//div[@class='detail']/span[2]/a/text()").extract()
        item["DetailedAddress"] = response.xpath("//div[@class='detail']/span[3]/text()").extract()
        
        
        item["Space"] = response.xpath("//span[@class='area']/text()").extract()
        item["Structure"] = response.xpath("//span[@class='type']/text()").extract()
        item["PricePerSquareMeter"] = response.xpath("//div[@class='price-panel pull-right']/h5/text()").extract()
        item["TotalPrice"] = response.xpath("//div[@class='price-panel pull-right']/span[@class='content']/text()").extract()
        item["Url"] = response.xpath("//div[@class='name-title clearfix']/a/@href").extract()
        yield item
        
        for i in range(1, 3):
            nexturl = "http://esf.fangdd.com/shenzhen/list/s1343_pa"+str(i)
            
            yield Request(nexturl, callback=self.parse, headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400"})
        
        
        
        
        
        
