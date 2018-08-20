
# -*- coding: utf-8 -*-
import scrapy
from ..items import DianyingItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["btrenren.com"]
    start_urls = [
    ]
    for x in range(1,794):
        a = "http://www.btrenren.com/index.php/Movie/index/order/time/p/"+str(x)+'.html'
        start_urls.append(a)


    def parse(self, response):#找到元素
        item = DianyingItem()

        zhi = ''
        for sel in response.xpath('/html/body/div[2]/div[2]/div/div[2]'):

            item['title'] = title =sel.xpath('h2/a/@title').extract()
            item['category'] = category =sel.xpath('ul/li[1]/a/@title').extract()
            item['area'] = area = sel.xpath('ul/li[2]/a/@title').extract()
            zhi = zhi + str(title+category+area)+'\n'
            yield item

        #with open('索引1','a') as f:
        #    f.write(zhi)