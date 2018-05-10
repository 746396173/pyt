# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['v2ex.com']
    start_urls = ['https://www.v2ex.com/']

    def parse(self, response):
        filename = "teacher.html"
        with open(filename,"wb+")as f_n:
            f_n.write(response.body)#写入的是二进制数据


