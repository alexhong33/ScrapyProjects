# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287']

    def parse(self, response):
        # 标题
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # 日期
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·", "").strip()
        # 点赞数
        praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]

        # 获取收藏数
        fav_nums = response.xpath("//span[cantain(@class, 'bookmark-btn']/text()").extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        # 获取评论数
        comment_nums = response.xpath("//a[@href='#article-comment']/span").extract()[0]
        match_re = re.match(".*(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)

        # 主体文章
        content = response.xpath("//div[@class='entry']").extract()[0]


        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)


        ###############################################################################################


        # 通过CSS选择器提取字段
        # 提取标题
        title = response.css(".entry-header h1::text").extract()
        # 提取日期
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·", " ").strip()
        # 提取点赞数
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]

        # 提取收藏数
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)


        # 提取评论数
        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.match(".*(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)


        # 提取主体文章
        content = response.css("div.entry").extract()[0]


        tags = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tags = [element for element in tags if not element.strip().endswith("评论")]
        tags = ",".join(tags)

        pass