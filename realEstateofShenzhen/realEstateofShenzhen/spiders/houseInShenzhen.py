# -*- coding: utf-8 -*-
import scrapy


class HouseinshenzhenSpider(scrapy.Spider):
    name = 'houseInShenzhen'
    allowed_domains = ['esf.fangdd.com/shenzhen']
    start_urls = ['http://esf.fangdd.com/shenzhen/']

    def parse(self, response):
        pass
