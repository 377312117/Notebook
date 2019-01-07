# -*- coding: utf-8 -*-
import scrapy


class BaiduPySpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        with open('Baidu.html','w',encoding='utf-8') as f:
            f.write(response.text)
    
    
