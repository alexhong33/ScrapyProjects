# -*- coding: utf-8 -*-
import scrapy


class QtspiderSpider(scrapy.Spider):
    name = 'qtspider'
    allowed_domains = ['58pic.com']
    start_urls = ['http://58pic.com/']

    def parse(self, response):
        pass
